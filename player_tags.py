class PlayerTagConverter:
    _alphabet = '0289PYLQGRJCUV'

    @classmethod
    def normalize_tag(cls, tag):
        tag = tag.strip().upper().removeprefix('#').replace('O', '0')
        if not tag or any(ch not in cls._alphabet for ch in tag):
            raise ValueError('Invalid player tag: use # followed by Supercell base-14 characters')
        return tag

    @classmethod
    def tag_to_id(cls, tag):
        total = 0
        for ch in cls.normalize_tag(tag):
            total = total * 14 + cls._alphabet.index(ch)
            if total > 0xffffffffff:
                raise ValueError('Player tag exceeds the high/low ID range')
        return total % 256, total // 256

    @classmethod
    def id_to_tag(cls, highID, lowID):
        if not 0 <= highID <= 255 or not 0 <= lowID <= 0xffffffff:
            raise ValueError('Invalid player ID')
        total = lowID * 256 + highID
        result = ''
        while total:
            total, digit = divmod(total, 14)
            result = cls._alphabet[digit] + result
        return '#' + (result or '0')


def profile_request(tag):
    import struct
    return struct.pack('>II', *PlayerTagConverter.tag_to_id(tag)) + b'\0'
