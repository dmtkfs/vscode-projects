import secrets
from tools.modify import rotate_list_left as rotateleft
from tools.modify import xor_bitlists as xor
from tools.modify import bits_to_bytes as tobytes


def primary_key_generator(keylength):
    firstpass = []
    secondpass = []
    randomizedkey = []

    for i in range(keylength):
        firstpass.append(secrets.randbits(1))
        secondpass.append(secrets.randbits(1))
        randomizedkey.append(firstpass[i] ^ secondpass[i])
    return randomizedkey


def roundkey_generator(mainkey, rounds):

    def sbox_generator():
        values = list(range(256))
        sbox = []
        while values:
            i = secrets.randbelow(len(values))
            sbox.append(values.pop(i))
        return sbox

    def use_sbox(bytes, sbox):
        return [sbox[byte] for byte in bytes]

    sbox = sbox_generator()
    roundkeys = []
    key_len = len(mainkey)

    for i in range(rounds):
        randombits = [secrets.randbits(1) for _ in range(key_len)]
        newkey = xor(mainkey, randombits)
        rotated_key = rotateleft(newkey, i)
        rotated_key = tobytes(rotated_key)
        transformed_key = use_sbox(rotated_key, sbox)
        roundkeys.append(transformed_key)

    return roundkeys
