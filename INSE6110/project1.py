import random
import time


# check if the number is prime
def is_prime(num):

    while True:  # check for primality

        if num == 0 or num == 1:  # known
            print(f"\n{num} is not prime.")
            return False  # not prime
        else:
            for i in range(2, num):  # check against all numbers including itself
                if num % i == 0:
                    print(f"\n{num} is not prime.")
                    return False  # not prime
            print(f"\n{num} is prime.\n")
            return True  # prime


# generate prime number for p and q
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
    return pow(
        e, -1, phi_N
    )  # return multiplicative inverse of e mod phi(N), which is our d


# works with both new and chosen primes p and q, to facilitate demonstration
def constant_generator(p=None, q=None):
    if not p and not q:
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
        print("")
    else:
        is_prime(p)
        print(f"p = {p}")
        is_prime(q)
        print(f"q = {q}")
        n = compute_n(p, q)
        print(f"N = {n}")
        phi_N = compute_phi_n(p, q)
        print(f"Phi(N) = {phi_N}")
        e = public_key_generator(phi_N)
        print(f"public key e = {e}")
        d = private_key_generator(e, phi_N)
        print(f"private key d = {d}")
        print("")


print("\nPart 1 - Computation\n==================================================\n")
constant_generator()

print(" General Computation Completed. Waiting...\n")
time.sleep(15)

constant_generator(p=49667, q=50177)
print(" Computation Completed for p = 49667 and q = 50177.")
print(" We have already chosen e = 1538624097 and d = 461365665. Waiting...\n")
time.sleep(15)

# My constants (saved):
# p = 49667
# q = 50177
my_N = 2492141059
# Phi(N) = 2492041216
# public key
my_e = 1538624097
# private key
d = 461365665

# Mikaeil Mayeli Feridani
N = 2496728609
e = 2423414819


def cut_to_chunks(message):  # cut the original message in 3-byte chunks

    cut_message = []  # initialize list

    while message:  # while there are characters left
        cut_message.append(message[:3])  # fill the list with 3-byte chunks
        message = message[3:]  # remove 3 characters from the original message

    cut_message = tuple(cut_message)  # convert to tuple for protection

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


def square_and_multiply(base, exponent, modulus):

    result = 1  # initialize the result.
    base = base % modulus  # optimization to avoid overflow.

    while exponent > 0:  # using exponent as counter.
        if exponent % 2 == 1:  # checking if the LSB is equal to 1.
            result = (
                result * base
            ) % modulus  # if it is, take the squared base and multiply it with base, then mod with N.
        exponent //= 2  # reduce the exponent.
        base = (
            base * base
        ) % modulus  # if the bit is -, square the base, then mod with N.

    return result


def encr_decr(N, e_or_d, text):

    converted_message = []

    for i in range(len(text)):
        converted_message.append(
            square_and_multiply(text[i], e_or_d, N)
        )  # fill the list with the encrypted/decrypted elements using square and multiply to handle big integers.

    converted_message = tuple(converted_message)  # convert to tuple for protection.

    return converted_message


def plain_text(decrypted_message):

    plaintext = ""  # initialize plaintext
    message_chunks = []

    for elem in decrypted_message:

        message_to_bytes = elem.to_bytes(
            (elem.bit_length() + 7) // 8, "big"
        )  # count neccessary bits for conversion and add 7 to round up for correct utf-8 representation
        # divide by 8 to properly convert to bytes, starting from MSB
        message_chunks.append(message_to_bytes.decode())
        plaintext += message_to_bytes.decode(
            "ascii", "ignore"
        )  # convert bytes to string and join them all together to form the plaintext

    print(f"The partner message in chunks is : {message_chunks}\n")

    return plaintext


def string_to_chunks(
    string, chunk_size
):  # split signature name to chunks in order to keep it smaller than N
    return [string[i : i + chunk_size] for i in range(0, len(string), chunk_size)]


def sign_and_check(N, d_or_e, m_or_sig):

    if isinstance(m_or_sig, str):
        # when the input is a string, divide it into chunks
        chunks = string_to_chunks(
            m_or_sig, 3
        )  # and assuming each chunk is 3 characters long
        print(f"My message to be signed in chunks is : {chunks}\n")

        chunks_int = []  # initialize
        for chunk in chunks:
            chunks_int.append(
                int.from_bytes(chunk.encode("utf-8"), byteorder="big")
            )  # convert str chunks to int chunks
        chunks_int = tuple(chunks_int)  # conversion to tuple
        print(f"Converted to be signed it is : {chunks_int}\n")

        signatures = tuple(
            square_and_multiply(chunk, d_or_e, N) for chunk in chunks_int
        )  # sign each chunk separately

        return signatures

    else:  # signature verification when input is an integer
        verified_signature = tuple(
            square_and_multiply(sig_chunk, d_or_e, N) for sig_chunk in m_or_sig
        )  # for each each chunk separately

        return verified_signature


def overall_verification(name, verify):
    verify_final = False  # initialization
    # combine all the chunks back together and verify the full signature
    verify_final = all(
        chunk_element == chunk_verification
        for chunk_verification, chunk_element in zip(
            verify,
            (
                int.from_bytes(chunk.encode("utf-8"), byteorder="big")
                for chunk in string_to_chunks(name, 3)
            ),  # using zip to compare the verification result for each chunk with its corresponding original chunk
        )
    )
    return verify_final


def main():

    message = "Hello Mikaeil!!"
    name = "Dimitrios Kafritsas"
    mikaeils_message = (
        552904839,
        202559165,
        832707405,
        607764759,
        38126602,
        2231604777,
    )
    signed_partner_text = (
        1483161003,
        2494912581,
        678708095,
        1785449489,
        498998315,
        1844286645,
        42096706,
        1071285895,
    )
    partner_name = "Mikaeil Mayeli Feridani"
    cut_message = cut_to_chunks(message)
    hex_chunks = hex_convert(cut_message)
    int_chunks = int_convert(hex_chunks)
    print(
        "\nPart 1 - Encryption/Decryption\n==================================================\n"
    )
    print(f"My original message is : {message}\n")
    print(f"In 3-byte chunks it is : {cut_message}\n")
    print(f"Converted to hex it is : {hex_chunks}\n")
    print(f"Converted to int it is : {int_chunks}\n")
    encrypted_message = encr_decr(N, e, int_chunks)
    print(f"My encrypted message is : {encrypted_message}\n")
    print(" Encryption Completed. Waiting...\n")
    time.sleep(15)
    decrypted_message = encr_decr(my_N, d, mikaeils_message)
    print(f"The decrypted partner message is : {decrypted_message}\n")
    plaintext = plain_text(decrypted_message)
    print(f"The original partner message is : {plaintext}\n")
    print(" Decryption Completed. Waiting...\n")
    time.sleep(15)
    print(
        "\nPart 2 - Signature & Verification\n==================================================\n"
    )
    print(f"My message to sign is : {name}\n")
    sign = sign_and_check(my_N, d, name)
    print(f"My signature is : {sign}\n")
    verify = sign_and_check(N, e, signed_partner_text)
    print(" Message Signed. Waiting...\n")
    time.sleep(15)
    print(f"The verified partner signature is : {verify}\n")
    print("Partner's Signature Verification\n================================")
    print(
        f"{partner_name}: {overall_verification(partner_name, verify)}\n================================\n"
    )
    print(" Signature Verified.\n")


main()
