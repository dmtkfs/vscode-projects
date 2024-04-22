import math
from tools.generators import generate_prime, generate_e_for_rsa
from RSA import rsa

x = int(input("Choose serial number: "))

p = generate_prime()
print(f"p = {p}")
q = generate_prime()
print(f"q = {q}")
n = p * q

r = int(input("Choose blinding factor: "))
while not math.gcd(r, n):
    r = int(input(f"gcd({r},{n}!= 1. Choose anoth blinding factor: "))

phin = (p - 1) * (q - 1)
print(f"Φ(N) = {phin}")
e = generate_e_for_rsa(phin)
print(f"e = {e}")

rsaresults = rsa("auto", p=p, q=q, e=e)
print(f"rsa results = {rsaresults}")

user_blind = (x * pow(r, e, n)) % n
blind_sign = pow(user_blind, rsaresults["private_key"], n)
user_unblind = (blind_sign * (pow(r, -1, n))) % n
print(f"sig = {user_unblind}")

verified_message = pow(user_unblind, e, n)
print("Verified message from signature:", verified_message == x)
