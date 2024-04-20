import math

m = int(input("Give m (the initial message): "))
p = int(input("Give p (the mod): "))
a1 = int(input("Give a1 (Alice's Choice): "))
b1 = int(input("Give b1 (Bob's Choice): "))

gcda = math.gcd(a1, p - 1)
print(f"gcd(a1,p) = {gcda}")
if gcda != 1:
    print("3-Pass DH Failed.")
    exit()
gcdb = math.gcd(b1, p - 1)
print(f"gcd(b1,p) = {gcdb}")
if gcdb != 1:
    print("3-Pass DH Failed.")
    exit()

a2 = pow(a1, -1, p - 1)
print(f"a2 = {a2}")

b2 = pow(b1, -1, p - 1)
print(f"b2 = {b2}")

msg = pow(m, a1 * b1 * a2 * b2, p)

if msg == m:
    print("3-Pass DH Completed Succesfully.")
    print(f"Initial msg was: {msg}")
else:
    print("3-Pass DH Failed.")
