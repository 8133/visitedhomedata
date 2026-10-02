import struct
from cryptography.hazmat.primitives.poly1305 import Poly1305
from nacl.bindings import crypto_scalarmult

SERVER_KEY = bytes.fromhex('8b1b04b927177aa53b07a217771fe6bc0a2c5d36cec6465b6c5c5148d051c546')
MASK = 0xffffffff


def rounds(state, count):
    x = list(state)
    def quarter(a, b, c, d):
        for dest, source, rotate in ((d, a, 16), (b, c, 12), (d, a, 8), (b, c, 7)):
            if dest == d:
                x[a] = (x[a] + x[b]) & MASK
            else:
                x[c] = (x[c] + x[d]) & MASK
            v = x[dest] ^ x[source]
            x[dest] = ((v << rotate) | (v >> (32-rotate))) & MASK
    for _ in range(count // 2):
        for q in ((0,4,8,12),(1,5,9,13),(2,6,10,14),
                  (3,7,11,15),(0,5,10,15),(1,6,11,12),(2,7,8,13),(3,4,9,14)):
            quarter(*q)
    return x


def hchacha18(key, nonce):
    if len(key) != 32 or len(nonce) != 16:
        raise ValueError('HChaCha18 requires a 32-byte key and 16-byte nonce')
    x = rounds(struct.unpack('<16I', b'expand 32-byte k' + key + nonce), 18)
    return struct.pack('<8I', *(x[i] for i in (0,1,2,3,12,13,14,15)))


def stream(key, nonce, length):
    if len(key) != 32 or len(nonce) != 24:
        raise ValueError('Expected a 32-byte key and 24-byte nonce')
    subkey = hchacha18(key, nonce[:16])
    result = bytearray()
    for counter in range((length+63)//64):
        initial = struct.unpack('<16I', b'expand 32-byte k'+subkey+struct.pack('<Q',counter)+nonce[16:])
        x = rounds(initial, 16)
        result.extend(struct.pack('<16I', *((a+b)&MASK for a,b in zip(x,initial))))
    return bytes(result[:length])


def shared_key(secret):
    return hchacha18(crypto_scalarmult(secret, SERVER_KEY), bytes(16))


def seal(plaintext, nonce, key):
    pad = stream(key, nonce, len(plaintext)+32)
    ciphertext = bytes(a^b for a,b in zip(plaintext,pad[32:]))
    return Poly1305.generate_tag(pad[:32], ciphertext) + ciphertext


def open_box(ciphertext, nonce, key):
    if len(ciphertext) < 16:
        raise ValueError('Ciphertext shorter than authentication tag')
    tag, body = ciphertext[:16], ciphertext[16:]
    pad = stream(key, nonce, len(body)+32)
    Poly1305.verify_tag(pad[:32], body, tag)
    return bytes(a^b for a,b in zip(body,pad[32:]))


def increment(nonce):
    return ((int.from_bytes(nonce, 'little')+2) % (1<<192)).to_bytes(24,'little')
