from tools.user_input import get_binary_input
from tools.checkers import check_valid_key_length
from tools.modify import array_split, xor_bitlists, bitpadding_plaintext, bits_to_bytes
from tools.generators import (
    generate_primary_key,
    generate_roundkey,
    generate_sbox,
)


def use_sbox(byte_array, sbox):
    return [sbox[byte] for byte in byte_array]


def feistel_round(rhalf, roundkey, sbox):
    rhalf_padded = bitpadding_plaintext(rhalf, len(roundkey))
    bitmix = xor_bitlists(rhalf_padded, roundkey)
    byte_array = bits_to_bytes(bitmix)
    sbox_output = use_sbox(byte_array, sbox)

    transformed_bits = [int(bit) for byte in sbox_output for bit in format(byte, "08b")]
    return transformed_bits[: len(rhalf)]


def feistel_encrypt(lhalf, rhalf, roundkeys, sbox):
    for roundkey in roundkeys:
        new_rhalf = [
            left ^ right
            for left, right in zip(lhalf, feistel_round(rhalf, roundkey, sbox))
        ]
        lhalf, rhalf = rhalf, new_rhalf
    return lhalf + rhalf


def feistel_decrypt(lhalf, rhalf, roundkeys, sbox):
    for roundkey in reversed(roundkeys):
        new_lhalf = [
            right ^ left
            for right, left in zip(rhalf, feistel_round(lhalf, roundkey, sbox))
        ]
        lhalf, rhalf = new_lhalf, lhalf
    return lhalf + rhalf


sbox = generate_sbox()
messagelength = int(input("Give message length: "))
inputbits = get_binary_input(messagelength)
rounds = int(input("How many rounds?: "))

lhalf, rhalf = array_split(inputbits)
print(f"Input split: {lhalf, rhalf}")

keylength = int(input("Choose key length (128-bit, 192-bit or 256-bit): "))
while not check_valid_key_length(keylength):
    keylength = int(
        input("Invalid choice. Choose key length (128-bit, 192-bit or 256-bit): ")
    )

primarykey = generate_primary_key(keylength)
print(f"Primary Key: {primarykey}")
roundkeys = generate_roundkey(primarykey, rounds, sbox)
print(f"Round Keys: {roundkeys}")

encrypted = feistel_encrypt(lhalf, rhalf, roundkeys, sbox)
decrypted = feistel_decrypt(*array_split(encrypted), roundkeys, sbox)

print(f"Initial input: {inputbits}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
print("Decryption successful:", decrypted == inputbits)
