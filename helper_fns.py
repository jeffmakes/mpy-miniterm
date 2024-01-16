import os
import uhashlib as hashlib
import ubinascii as binascii

def sha256(fn):
    hash_sha256 = hashlib.sha256()
    try:
        f = open(fn, 'rb')
        while True:
            c = f.read(1024)
            if not c:
                break
            hash_sha256.update(c)
        return binascii.hexlify(hash_sha256.digest())
    except OSError:
        return None
