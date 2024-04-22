def check_isprime(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return 0
    return 1


def check_valid_key_length(keylength):
    return keylength == 128 or keylength == 192 or keylength == 256


def check_binary_array(array, length):
    if len(array) != length:
        return False
    return all(str(b) in "01" for b in array)


def check_if_3mod4(n):
    three = n % 4
    return three == 3
