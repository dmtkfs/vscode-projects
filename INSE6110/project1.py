"""
import random


# Randomly select two prime numbers, denoted by p and q (16 bits each)
# check if the number is prime
def is_prime(num):

    while True:  # check for primality

        if num == 0 or num == 1:  # known
            return False  # not prime
        else:
            for i in range(2, num):  # check against all numbers including itself
                if num % i == 0:
                    return False  # not prime

            return True  # prime


# generate number
def prime_generator():

    number = random.randint(0, 65535)  # 16bits = 65535 including 0
    gen_num = is_prime(number)  # to check generated number

    while True:

        if gen_num:  # if the number is prime keep it
            return number
        else:  # if not, generate new number
            number = random.randint(0, 65535)
            gen_num = is_prime(number)  # and check it


def compute_n(p, q):
    return p * q


def compute_phi_n(p, q):
    return (p - 1) * (q - 1)


def gcd(big, small):

    new_big = small  # the new big number is the previous small number; initialization in temp variable
    new_small = (
        big % small
    )  # the new small number is the remainder of the division; initialization in temp variable

    while True:  # loop until we get to the gcd
        new_big = (
            small  # the new big number is the previous small number in temp variable
        )
        new_small = (
            big % small
        )  # the new small number is the remainder of the division in temp variable
        big = new_big  # assign the change to the real variable
        small = new_small  # assign the change to the real variable

        if new_small == 0:  # if we reach the end
            return new_big  # return the gcd


def public_key_generator(phi_N):

    e = random.randint(1, phi_N - 1)  # generate random e value such that e < phi(N)

    while True:

        if gcd(phi_N, e) == 1:  # check if gcd(e, Phi(N)) = 1)
            return e  # if yes, keep e
        else:  # if not, generate new e
            e = random.randint(1, phi_N - 1)


def private_key_generator(e, phi_N):  # we already know that gcd(pk)e, phi(N) = 1
    return pow(e, -1, phi_N)  # return multiplicative inverse of e mod phi(N)


def constant_generator():
    p = prime_generator()
    print(f"p = {p}")
    q = prime_generator()
    print(f"q = {q}")
    n = compute_n(p, q)
    print(f"N = {n}")
    phi_N = compute_phi_n(p, q)
    print(f"Phi(N) = {phi_N}")
    e = public_key_generator(phi_N)
    print(f"public key e = {e}")
    d = private_key_generator(e, phi_N)
    print(f"private key d = {d}")


constant_generator()
"""

# Mine:
# p = 49667
# q = 50177
# N = 2492141059
# Phi(N) = 2492041216
# public key e = 1538624097
# private key d = 461365665

# Mikaeil Mayeli Feridani
# N: 	2496728609
# e: 	2423414819


def cut_to_chunks(message):  # cut the original message in 3-byte chunks

    cut_message = []  # initialize list

    while message:  # while there are characters left
        cut_message.append(message[:3])  # fill the list with 3-byte chunks
        message = message[3:]  # remove 3 characters from the original message

    cut_message = tuple(cut_message)

    return cut_message  # return the processed message


def hex_convert(cut_message):  # convert the 3-byte chunks to hexadecimal string

    hex_chunks = []  # initialize list
    hex_chunks = [
        "0x" + "".join(hex(ord(char))[2:] for char in string) for string in cut_message
    ]  # add the hexadecimal outside the expression so it gets added only once, the join it in front of the converted element to complete the hex conversion.
    # we start from the 3rd element in the ord list to avoid each 0x then join it at the end to keep the proper hex format.

    hex_chunks = tuple(hex_chunks)  # convert to tuple for protection

    return hex_chunks


def int_convert(hex_chunks):  # convert the 3-byte chunks to int string

    int_chunks = [
        int(val, 16) for val in hex_chunks
    ]  # convert every hex element in the tuple to an int element

    int_chunks = tuple(int_chunks)  # convert to tuple for protection

    return int_chunks


def main():

    message = "Hello Mikaeil!!"

    cut_message = cut_to_chunks(message)
    hex_chunks = hex_convert(cut_message)
    int_chunks = int_convert(hex_chunks)
    print("")
    print(f"The original message is: {message}\n")
    print(f"In 3-byte chunks it is : {cut_message}\n")
    print(f"Converted to hex it is : {hex_chunks}\n")
    print(f"Converted to int it is : {int_chunks}\n")


main()
