import secrets
import random
import math
from tools.checkers import check_isprime
from tools.modify import rotate_list_bytes
from tools.modify import bits_to_bytes


def generate_prime(bits=16):
    if bits < 2:
        raise ValueError("Number of bits must be 2 or more.")

    while True:
        n = random.getrandbits(bits)
        n |= (1 << bits - 1) | 1

        if check_isprime(n):
            return n


def generate_e_for_rsa(phin):
    e = 0
    while e <= 1 or e >= phin or math.gcd(e, phin) != 1:
        e = random.randint(1, phin)
    return e


def generate_primary_key(keylength):
    return [secrets.randbits(1) for _ in range(keylength)]


def generate_sbox():
    values = list(range(256))
    sbox = []
    while values:
        i = secrets.randbelow(len(values))
        sbox.append(values.pop(i))
    return sbox


def generate_roundkey(mainkey, rounds, sbox):
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


def generate_polynomial_for_secret(secret, k, p):
    coefficients = [secret] + [random.randint(0, p - 1) for _ in range(k - 1)]
    return coefficients
