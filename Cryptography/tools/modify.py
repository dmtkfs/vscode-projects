def array_split(inputarray):
    mid = len(inputarray) // 2
    return inputarray[:mid], inputarray[mid:]


def rotate_list_left(bit_list, shift):
    shift %= len(bit_list)
    return bit_list[shift:] + bit_list[:shift]


def xor_bitlists(list1, list2):
    return [a ^ b for a, b in zip(list1, list2)]


def bits_to_bytes(bits):
    bytes = []
    for i in range(0, len(bits), 8):
        byte = 0
        for bit in bits[i : i + 8]:
            byte = (byte << 1) | bit
        bytes.append(byte)
    return bytes


def bitpadding_plaintext(bitlist, target_length):
    return (
        bitlist + [0] * (target_length - len(bitlist))
        if len(bitlist) < target_length
        else bitlist
    )


def bitpadding_plaintext(bitlist, target_length):
    return (
        bitlist + [0] * (target_length - len(bitlist))
        if len(bitlist) < target_length
        else bitlist[:target_length]
    )
