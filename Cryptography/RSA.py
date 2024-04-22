import math
from tools.checkers import check_isprime as isprime


def rsa(flag="auto", c=0, m=0, p=None, q=None, e=None):
    results = {}

    if flag == "manual":
        c = int(input("Give c (the ciphertext). Give 0 if not applicable: "))
        m = int(input("Give m (the plaintext). Give 0 if not applicable: "))
        p = int(input("Give p (prime generator): "))
        while not isprime(p):
            p = int(input("p not prime. Give a prime number: "))
        q = int(input("Give q (prime generator): "))
        while not isprime(q):
            q = int(input("q not prime. Give a prime number: "))
        e = int(input("Give e (encryption exponent): "))
        while e <= 1 or e >= (p - 1) * (q - 1) or math.gcd(e, (p - 1) * (q - 1)) != 1:
            e = int(
                input("must be 1 < e < Φ(n) and gcd(e,Φ(n) must be 1. Give new e: ")
            )
    elif not all([p, q, e]):
        raise ValueError("All parameters must be provided for auto mode.")

    n = p * q
    phin = (p - 1) * (q - 1)
    d = pow(e, -1, phin)

    results["public_key"] = (e, n)
    results["private_key"] = d

    if c:
        plaintext = pow(c, d, n)
        results["plaintext"] = plaintext

    if m:
        ciphertext = pow(m, e, n)
        results["ciphertext"] = ciphertext

    return results


if __name__ == "__main__":
    result = rsa("manual")
    print(f"The result is: {result}")
