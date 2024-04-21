def array_split(inputarray):
    mid = len(inputarray) // 2
    left_half = inputarray[:mid]
    right_half = inputarray[mid:]
    leftarray = [int(bit) for bit in left_half]
    rightarray = [int(bit) for bit in right_half]

    return leftarray, rightarray


def rotate_list_left(bit_list, shift):
    shift %= len(bit_list)
    return bit_list[shift:] + bit_list[:shift]


def xor_bitlists(list1, list2):
    return [a ^ b for a, b in zip(list1, list2)]


def bits_to_bytes(bits):
    padding_length = (8 - len(bits) % 8) % 8
    padded_bits = bits + [0] * padding_length
    bytes = []

    for i in range(0, len(padded_bits), 8):
        byte = 0
        for bit in padded_bits[i : i + 8]:
            byte = (byte << 1) | bit
        bytes.append(byte)

    return bytes
