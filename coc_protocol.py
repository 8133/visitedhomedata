import struct


def i32(value):
    return struct.pack('>i', value)


def sc_string(value):
    if value is None:
        return i32(-1)
    encoded = value.encode('utf-8')
    return i32(len(encoded)) + encoded


def frame(message_id, payload, version=0):
    if len(payload) > 0xffffff:
        raise ValueError('Frame payload exceeds the 24-bit length field')
    return struct.pack('>H', message_id) + len(payload).to_bytes(3, 'big') + struct.pack('>H', version) + payload


def recv_exact(sock, size):
    result = bytearray()
    while len(result) < size:
        chunk = sock.recv(size - len(result))
        if not chunk:
            raise EOFError(f'Server closed connection after {len(result)}/{size} bytes')
        result.extend(chunk)
    return bytes(result)


def recv_frame(sock, maximum=4 * 1024 * 1024):
    header = recv_exact(sock, 7)
    message_id = int.from_bytes(header[:2], 'big')
    length = int.from_bytes(header[2:5], 'big')
    version = int.from_bytes(header[5:], 'big')
    if length > maximum:
        raise ValueError(f'Refusing oversized frame: {length} bytes')
    return message_id, version, recv_exact(sock, length)


def describe(message_id, version, payload):
    names = {20100: 'ServerHello', 20103: 'LoginFailed', 23654: 'LoginOk', 25195: 'OwnHomeData', 26443: 'AvatarProfile'}
    result = {'id': message_id, 'name': names.get(message_id, 'Unknown'),
              'version': version, 'length': len(payload), 'payload_hex': payload.hex()}
    if message_id == 20100 and len(payload) >= 4:
        length = struct.unpack('>i', payload[:4])[0]
        if 0 <= length <= len(payload) - 4:
            result['session_token_hex'] = payload[4:4+length].hex()
            result['remaining_hex'] = payload[4+length:].hex()
    return result
