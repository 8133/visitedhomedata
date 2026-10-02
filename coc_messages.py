import json
import struct
import zlib


class Reader:
    def __init__(self, data):
        self.data, self.pos = data, 0

    def take(self, size):
        if size < 0 or size > len(self.data)-self.pos:
            raise ValueError('Truncated or invalid message field')
        value = self.data[self.pos:self.pos+size]
        self.pos += size
        return value

    def integer(self):
        return struct.unpack('>i', self.take(4))[0]

    def blob(self):
        n = self.integer()
        if n == -1:
            return None
        return self.take(n)

    def string(self):
        b = self.blob()
        return None if b is None else b.decode('utf-8')

    def long(self):
        return list(struct.unpack('>II', self.take(8)))

    def vint(self):
        first = self.take(1)[0]
        negative = bool(first & 64)
        value, shift, current = first & 63, 6, first
        for _ in range(4):
            if not current & 128:
                return value - (1 << shift) if negative else value
            current = self.take(1)[0]
            value |= (current & 127) << shift
            shift += 7
        if current & 128:
            raise ValueError('Overlong VInt')
        value = value - (1 << shift) if negative else value
        if not -(1<<31) <= value < (1<<31):
            raise ValueError('VInt exceeds int32 range')
        return value


def compressed_json(data, maximum=8*1024*1024):
    if len(data)<4:
        raise ValueError('Compressed JSON is missing its length prefix')
    expected = int.from_bytes(data[:4], 'little')
    if expected > maximum:
        raise ValueError('Compressed JSON exceeds decoded-size limit')
    decompressor = zlib.decompressobj()
    raw = decompressor.decompress(data[4:], maximum+1)
    if len(raw) != expected or not decompressor.eof or decompressor.unused_data not in (b'',b'\0'):
        raise ValueError('Invalid compressed JSON size or stream')
    return json.loads(raw)


def login_failure(data):
    r = Reader(data)
    result = {'error_code':r.integer()}
    for name in ('fingerprint_string','host','message','update_url','extra'):
        result[name] = r.string()
    result['retry_seconds'] = r.integer()
    result['flag'] = r.take(1)[0] & 1
    packed = r.blob()
    if packed:
        result['fingerprint'] = compressed_json(packed)
    return result


def login_account(data):
    r = Reader(data)
    result = {'account_id':r.long(), 'home_id':r.long(), 'pass_token':r.string()}
    if not result['pass_token']:
        raise ValueError('LoginOk did not contain an account token')
    return result


def home_data(data, header_count):
    r = Reader(data)
    result = {'header_ints':[r.integer() for _ in range(header_count)], 'home_id':r.long(),
              'home_ints':[r.integer() for _ in range(4)]}
    compressed = bool(r.take(1)[0] & 1)
    home = r.blob()
    if home is None:
        result['home'] = None
    elif compressed:
        result['home'] = compressed_json(home)
    else:
        result['home'] = json.loads(home)
    result['decoded_prefix_bytes'] = r.pos
    result['remaining_bytes'] = len(data)-r.pos
    return result


def own_home(data):
    return home_data(data, 3)


def avatar_profile(data):
    r = Reader(data)
    avatar_id, home_id = r.long(), r.long()
    candidates = []
    for pos in range(8, len(data)-2):
        if data[pos] != 0x78 or (data[pos]*256+data[pos+1]) % 31:
            continue
        size = int.from_bytes(data[pos-8:pos-4], 'big', signed=True)
        if size < 6 or size > len(data)-(pos-4):
            continue
        expected = int.from_bytes(data[pos-4:pos], 'little')
        if expected > 8*1024*1024:
            continue
        try:
            home = compressed_json(data[pos-4:pos-4+size])
        except (ValueError,zlib.error):
            continue
        if isinstance(home,dict) and isinstance(home.get('buildings'),list):
            candidates.append((pos-8,size,home))
    if len(candidates) != 1:
        raise ValueError(f'Expected one framed home JSON in AvatarProfile, found {len(candidates)}; raw response saved')
    offset, size, home = candidates[0]
    return {'avatar_id':avatar_id,'home_id':home_id,
            'home':home,'home_blob_offset':offset,'home_blob_length':size,
            'avatar_bytes':offset,'remaining_bytes':len(data)-(offset+4+size)}


def avatar_profile_failure(data):
    r = Reader(data)
    return {'avatar_id':r.long(), 'error_code':r.vint()}
