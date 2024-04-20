import math
from tools.checkers import isprime as isprime

c = int(input("Give c (the ciphertext). Give 0 if not applicable: "))
m = int(input("Give m (the plaintext). Give 0 if not applicable: "))
p = int(input("Give p (prime generator): "))
primep = isprime(p)
while not primep:
    p = int(input("p not prime. Give a prime number: "))
    primep = isprime(p)
q = int(input("Give q (prime generator): "))
primeq = isprime(q)
while not primeq:
    q = int(input("q not prime. Give a prime number: "))
    primeq = isprime(q)
n = p * q
phin = (p - 1) * (q - 1)
print(f"Φ(n) = {phin}")
e = int(input("Give e (encryption exponent): "))
if e <= 1 or e >= phin or math.gcd(e, phin) != 1:
    e = int(input("must be 1 < e < Φ(n) and gcd(e,Φ(n) must be 1. Give new e: "))
    while e <= 1 or e >= phin or math.gcd(e, phin) != 1:
        e = int(input("must be 1 < e < Φ(n) and gcd(e,Φ(n) must be 1. Give new e: "))
d = pow(e, -1, phin)
print(f"public key (e,n) is: {e,n}")
print(f"public key (d) is: {d}")

if c:
    plaintext = pow(c, d, n)
    print(f"The plaintext is: {plaintext}")
if m:
    ciphertext = pow(m, e, n)
    print(f"The ciphertext is: {ciphertext}")
