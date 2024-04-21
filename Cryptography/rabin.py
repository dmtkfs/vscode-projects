from tools.checkers import check_isprime, check_if_3mod4
from tools.math_assist import sqrt_x_mod_n
from CRT import crt


p = int(input("Give p (prime) equal to 3 mod 4: "))
while not check_isprime(p) or not check_if_3mod4(p):
    p = int(input("p not prime or p != 3 mod 4. Give new p: "))

q = int(input("Give q (prime) equal to 3 mod 4: "))
while not check_isprime(q) or not check_if_3mod4(q):
    q = int(input("q not prime or q != 3 mod 4. Give new q: "))

n = p * q

message = int(input("Give message: "))
while message >= n:
    message = int(input(f"message too long. Give message smaller than {n}: "))

print(f"plaintext: {message}")
ciphertext = pow(message, 2, n)
print(f"ciphertext: {ciphertext}")


def decrypt(ciphertext, p, q):
    root_p1 = sqrt_x_mod_n(ciphertext, p)
    root_p2 = (p - root_p1) % p

    root_q1 = sqrt_x_mod_n(ciphertext, q)
    root_q2 = (q - root_q1) % q

    plaintexts = []
    for root_p in [root_p1, root_p2]:
        for root_q in [root_q1, root_q2]:
            result = crt("auto", [root_p, root_q], [p, q])
            plaintexts.append(result)

    return plaintexts


plaintexts = decrypt(ciphertext, p, q)
print(f"Possible plaintexts: {plaintexts}")
