def basic_hash(message, size=16):
    prime = 3
    size = pow(2, size)
    hash = 0
    if isinstance(message, int):
        input_bytes = message.to_bytes(
            (message.bit_length() + 7) // 8, byteorder="big", signed=True
        )
        for byte in input_bytes:
            hash = (hash * prime + byte) % size
    elif isinstance(message, str):
        for char in message:
            char_code = ord(char)
            hash = (hash * prime + char_code) % size
    else:
        raise TypeError("Unsupported input type: Input must be an integer or string")

    return hash


def verify_integrity(original_data, stored_hash):
    new_hash = basic_hash(original_data, hashsize)
    if new_hash == stored_hash:
        return True
    else:
        return False


message = input("Give your message for hashing: ")
hashsize = int(input("Give hash size: "))
while hashsize <= 0:
    hashsize = int(input("Size must be positive. Give hash size: "))

hash = basic_hash(message, hashsize)
print(f"The message '{message}' was hashed to {hash}.")

print(
    f"The hash '{hash}' belongs to the message '{message}': {verify_integrity(message, hash)}"
)
