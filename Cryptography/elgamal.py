import secrets
from tools.checkers import check_isprime


p = int(input("Give p (prime): "))
while not check_isprime(p):
    p = int(input("p not prime. Give new p: "))
print(f"p = {p}")

message = int(input("Give message: "))
while message <= 0 or message >= p:
    message = int(input("message must be positive and less than p. Give new message: "))

g = int(input("Give g: "))
while g <= 0 or g >= p:
    g = int(input("g must be positive and less than p. Give new g: "))
print(f"g = {g}")

x = int(input("Give x (private key, should be less than p): "))
while x <= 0 or x >= p:
    x = int(input("x must be positive and less than p. Give new x: "))
print(f"x = {x}")

y = pow(g, x, p)
print(f"y = {y}")

k = secrets.randbelow(p - 1) + 1
print(f"k = {k}")

r = pow(g, k, p)

r = pow(g, k, p)
c = (message * pow(y, k, p)) % p
ciphertext = [r, c]
print(f"ciphertext: {ciphertext}")

plaintext = (c * pow(r, p - 1 - x, p)) % p
print(f"plaintext: {plaintext}")
