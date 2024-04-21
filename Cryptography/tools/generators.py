import secrets
from tools.modify import rotate_list_bytes
from tools.modify import bits_to_bytes


def primary_key_generator(keylength):
    return [secrets.randbits(1) for _ in range(keylength)]


def sbox_generator():
    values = list(range(256))
    sbox = []
    while values:
        i = secrets.randbelow(len(values))
        sbox.append(values.pop(i))
    return sbox


def use_sbox(byte_array, sbox):
    return [sbox[byte] for byte in byte_array]


def roundkey_generator(mainkey, rounds, sbox):
    roundkeys = []
    for i in range(rounds):
        randombits = [secrets.randbits(1) for _ in range(len(mainkey))]
        newkey = [a ^ b for a, b in zip(mainkey, randombits)]
        newkey_bytes = bits_to_bytes(newkey)
        transformed_bytes = use_sbox(newkey_bytes, sbox)
        rotated_bytes = rotate_list_bytes(transformed_bytes, i)
        transformed_bits = [
            int(bit) for byte in rotated_bytes for bit in format(byte, "08b")
        ]
        roundkeys.append(transformed_bits[: len(mainkey)])
    return roundkeys
