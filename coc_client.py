import argparse
import base64
import hashlib
import json
import os
from pathlib import Path
import secrets
import socket
import struct
import sys
import uuid

from nacl.bindings import crypto_scalarmult_base
from cryptography.exceptions import InvalidSignature
from coc_crypto import SERVER_KEY, shared_key, seal, open_box, increment
from coc_protocol import frame, recv_frame, sc_string, i32, describe
from coc_messages import login_account, login_failure, own_home, avatar_profile, avatar_profile_failure
from player_tags import PlayerTagConverter, profile_request


def vint(value):
    negative = value < 0
    value &= 0xffffffff
    first = (value & 63) | (64 if negative else 0)
    value >>= 6
    if negative:
        value |= ~0x3ffffff
    out = bytearray()
    while (value != -1 if negative else value != 0):
        out.append(first | 128)
        first = value & 127
        value >>= 7
    out.append(first)
    return bytes(out)


def login_payload(sha, device_id, account=None):
    fields = [
        struct.pack('>II', *(account['account_id'] if account else (0,0))),
        sc_string(account['pass_token'] if account else None),
        vint(18), vint(600), i32(0), vint(7),
        sc_string(sha),
        sc_string(device_id),
        sc_string(None),
        sc_string('Android'),
        sc_string('14'),
        i32(0),
        sc_string('en'),
        sc_string(None),
        sc_string(device_id),
        b'\x01',
        sc_string(''), sc_string(''), sc_string(''),
        b'\x00',
        sc_string(''),
        i32(0), vint(2),
        sc_string(''), sc_string(''),
        sc_string('18.600.7'),
        sc_string(''), sc_string(''), vint(0),
        i32(-1),
        sc_string(''),
        sc_string(''), sc_string(''), i32(-1),
        sc_string(''), sc_string(''), sc_string(''), sc_string(''),
        sc_string(''),
        b'\x00',
        sc_string(''),
        b'\x00',
    ]
    return b''.join(fields)


def save_private(path, data):
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, 'wb') as f:
        f.write(data)


def create_output_directory(base):
    base = Path(base)
    candidate = base
    index = 0
    while True:
        try:
            candidate.mkdir(mode=0o700)
            return candidate
        except FileExistsError:
            index += 1
            candidate = base.with_name(f'{base.name}-{index:03d}')


def select_account(reuse, account_path, output):
    if reuse is None:
        if account_path:
            raise ValueError('--account requires --reuse; omit both for a new account')
        return None
    if account_path or reuse != 'latest':
        path = Path(account_path or reuse)
        if path.is_dir():
            path = path/'account.json'
    else:
        base = Path(output)
        candidates = []
        for directory in base.parent.iterdir():
            suffix = directory.name.removeprefix(base.name+'-')
            matches = directory.name == base.name or (
                directory.name.startswith(base.name+'-') and suffix.isdigit())
            path = directory/'account.json'
            if matches and directory.is_dir() and path.is_file():
                candidates.append(path)
        if not candidates:
            raise ValueError('No saved account found; run without --reuse first or use --reuse PATH')
        path = max(candidates, key=lambda item: (
            item.stat().st_mtime_ns,
            0 if item.parent.name == base.name else int(item.parent.name[len(base.name)+1:])))
    account = json.loads(path.read_text())
    struct.pack('>II', *account['account_id'])
    if not isinstance(account['pass_token'],str) or not account['pass_token']:
        raise ValueError('Invalid account pass token')
    return account


class LoginRejected(Exception):
    def __init__(self, details):
        self.details = details
        super().__init__(f"LoginFailed error {details['error_code']}")


def rejected(data, out):
    save_private(out/'login_failed.bin',data)
    details = login_failure(data)
    printable = {k:v for k,v in details.items() if k != 'fingerprint'}
    if 'fingerprint' in details:
        printable['fingerprint_sha'] = details['fingerprint']['sha']
        printable['fingerprint_version'] = details['fingerprint'].get('version')
    print(json.dumps({'id':20103,'name':'LoginFailed',**printable}),flush=True)
    raise LoginRejected(details)


def run_session(args, out, fp, account, device_id):
    client_secret = secrets.token_bytes(32)
    public = crypto_scalarmult_base(client_secret)
    key = shared_key(client_secret)
    client_nonce = bytearray(secrets.token_bytes(24))
    client_nonce[0] &= 254
    client_nonce = bytes(client_nonce)
    payload = login_payload(fp['sha'], device_id, account)
    hello = b''.join(i32(n) for n in (3,151,18,600,7)) + sc_string(fp['sha'])
    hello += i32(2)+i32(2)+i32(0)+sc_string('')
    with socket.create_connection((args.host,args.port),timeout=args.timeout) as sock:
        sock.sendall(frame(10100,hello))
        msg, version, data = recv_frame(sock)
        print(json.dumps(describe(msg,version,data),indent=2),flush=True)
        if msg != 20100 or len(data) != 28 or data[:4] != i32(24):
            raise ValueError('Expected ServerHello with a 24-byte session token')
        token = data[4:]
        nonce = hashlib.blake2b(public+SERVER_KEY,digest_size=24).digest()
        encrypted = public+seal(token+client_nonce+payload,nonce,key)
        sock.sendall(frame(10101,encrypted,12))
        print('Sent LoginMessage (10101, version 12)',file=sys.stderr,flush=True)
        authenticated = False
        profile_sent = False
        session_key = server_nonce = None
        for index in range(64):
            msg, version, data = recv_frame(sock)
            save_private(out/f'{index:02d}-{msg}.wire.bin',data)
            if not authenticated:
                if msg == 20103 and data[:4] in [i32(x) for x in range(1,40)]:
                    rejected(data,out)
                if msg not in (20103,23654):
                    raise ValueError(f'Expected LoginOk/LoginFailed, got {msg}')
                nonce = hashlib.blake2b(client_nonce+public+SERVER_KEY,digest_size=24).digest()
                plain = open_box(data,nonce,key)
                if len(plain) < 56:
                    raise ValueError('Login response missing negotiated nonce/key')
                server_nonce, session_key, data = plain[:24],plain[24:56],plain[56:]
                if msg == 20103:
                    rejected(data,out)
                authenticated = True
                save_private(out/'login_ok.bin',data)
                returned = login_account(data)
                returned['device_id'] = device_id
                save_private(Path(args.output)/'account.json',json.dumps(returned,indent=2).encode())
                print(json.dumps({'id':msg,'name':'LoginOk','version':version,'length':len(data),
                                  'account_id':returned['account_id'],
                                  'credentials_file':str(Path(args.output)/'account.json')}),flush=True)
                continue
            server_nonce = increment(server_nonce)
            data = open_box(data,server_nonce,session_key)
            save_private(out/f'{index:02d}-{msg}.bin',data)
            record = {'id':msg,'version':version,'length':len(data)}
            if args.tag and profile_sent and msg == 20206:
                decoded = avatar_profile_failure(data)
                save_private(Path(args.output)/'avatar_profile_failed.json',json.dumps(decoded,indent=2).encode())
                print(json.dumps({'name':'AvatarProfileFailed',**record,**decoded}),flush=True)
                raise ValueError(f"Profile request failed with error {decoded['error_code']}")
            if args.tag and msg == 25195 and not profile_sent:
                client_nonce = increment(client_nonce)
                sock.sendall(frame(11734, seal(profile_request(args.tag), client_nonce, session_key)))
                profile_sent = True
                print(json.dumps({'event':'AskForAvatarProfile','id':11734,'tag':args.tag}),flush=True)
                continue
            if args.tag and profile_sent and msg == 26443:
                save_private(Path(args.output)/'avatar_profile.bin',data)
                decoded = avatar_profile(data)
                if decoded['avatar_id'] != list(PlayerTagConverter.tag_to_id(args.tag)):
                    raise ValueError('AvatarProfile ID does not match requested tag')
                decoded['tag'] = args.tag
                save_private(Path(args.output)/'avatar_profile.json',json.dumps(decoded,indent=2).encode())
                save_private(Path(args.output)/'profile_home.json',json.dumps(decoded['home'],indent=2).encode())
                record.update(name='AvatarProfile', **decoded)
                if args.raw:
                    record['payload_base64'] = base64.b64encode(data).decode()
                print(json.dumps(record,indent=2),flush=True)
                return 0
            if msg == 25195:
                if args.tag:
                    continue
                save_private(Path(args.output)/'own_home.bin',data)
                decoded = own_home(data)
                save_private(Path(args.output)/'own_home.json',json.dumps(decoded,indent=2).encode())
                record.update(name='OwnHomeData', **decoded)
                if args.raw:
                    record['payload_base64'] = base64.b64encode(data).decode()
                print(json.dumps(record,indent=2),flush=True)
                return 0
            print(json.dumps(record),flush=True)
        raise ValueError('Requested home data not received within 64 messages')


def main():
    p = argparse.ArgumentParser(
        description='get clash of clans base data from a tag without emulator or apk! fingerprint is built in. tested on coc 18.600.7. makes a new account unless you use --reuse.',
        add_help=False)
    p.add_argument('-h', '--help', action='help', help='show this help and exit')
    p.add_argument('--host', default='gamea.clashofclans.com', metavar='host', help='server to connect to (default: gamea.clashofclans.com)')
    p.add_argument('--port', type=int, default=9339, metavar='port', help='server port (default: 9339)')
    p.add_argument('--reuse', nargs='?', const='latest', metavar='path',
                   help='reuse the last saved account, or give it an account.json path or session folder')
    p.add_argument('--account', metavar='path', help='pick an account.json to use with --reuse')
    p.add_argument('--tag', metavar='tag', help='player tag to get base data from, like "#2PP"')
    p.add_argument('--raw', action='store_true', help='also print the full decrypted response as base64')
    p.add_argument('--output', default='client-session', metavar='folder', help='where to save the data (default: client-session), adds a number if it already exists')
    p.add_argument('--timeout', type=float, default=20, metavar='seconds', help='how long to wait for the server (default: 20 seconds)')
    args = p.parse_args()
    if args.tag:
        try:
            args.tag = PlayerTagConverter.id_to_tag(*PlayerTagConverter.tag_to_id(args.tag))
        except ValueError as exc:
            p.error(str(exc))
    if args.timeout <= 0:
        p.error('--timeout must be positive')
    if args.account and args.reuse is None:
        p.error('--account requires --reuse; omit both for a new account')
    if args.account and args.reuse != 'latest':
        p.error('use --reuse path or --reuse --account path, not both')
    try:
        fp = {'sha': '7839fe492f55e0c5cb096b788649cd82f2a99f01', 'version': '18.600.6'}
        account = select_account(args.reuse, args.account, args.output)
        device_id = account.get('device_id',str(uuid.uuid4())) if account else str(uuid.uuid4())
        out = create_output_directory(args.output)
        args.output = str(out)
        print(f"Account mode: {'reuse' if account else 'new'}; output: {out}",file=sys.stderr,flush=True)
        for attempt in range(2):
            session = out/f'attempt-{attempt+1}'
            session.mkdir(mode=0o700)
            save_private(session/'fingerprint.json',json.dumps(fp).encode())
            try:
                return run_session(args,session,fp,account,device_id)
            except LoginRejected as exc:
                supplied = exc.details.get('fingerprint')
                if attempt==0 and exc.details['error_code']==7 and supplied and supplied['sha']!=fp['sha']:
                    fp = supplied
                    save_private(out/'server-fingerprint.json',json.dumps(fp).encode())
                    print('got the fingerprint from the server, reconnecting with it.',file=sys.stderr)
                    continue
                raise
    except (OSError,EOFError,ValueError,KeyError,TypeError,struct.error,InvalidSignature,LoginRejected) as exc:
        print(f'Client failed: {type(exc).__name__}: {exc}',file=sys.stderr)
        return 1


if __name__=='__main__':
    sys.exit(main())