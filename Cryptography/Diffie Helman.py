p = 0
g = 0
a = 0
b = 0

p = int(input("Give p (the mod): "))
g = int(input("Give g (the parameter): "))
while g >= p - 1:
    g = int(input("g >= p-1. Give g < p-1: "))
a = int(input("Give a (Alice's Choice): "))
while a >= p:
    a = int(input("a > p. Give a < p: "))
b = int(input("Give b (Bob's Choice): "))
while b >= p:
    b = int(input("b > p. Give b < p: "))

key = pow(g, a * b, p)
print(f"The Key is: {key}")
