from tools.math_assist import croot

congruences = 0
variableindex = []
modindex = []
globalmod = 1
sum = 0
while congruences != 2 and congruences != 3:
    congruences = int(input("Number of congruences? Choose 2 or 3: "))

for i in range(congruences):
    variableindex.append(int(input(f"Give variable for congruence {i+1}: ")))
    modindex.append(int(input(f"Give mod for congruence {i+1}: ")))
    globalmod = globalmod * modindex[i]
for i in range(congruences):
    print(f"Congruence {i+1}: X = {variableindex[i]} mod {modindex[i]}")
print("Solving for X:")
if congruences == 2:
    for i in range(congruences):
        if i == 0:
            sum += (
                variableindex[i]
                * modindex[i + 1]
                * pow(modindex[i + 1], -1, modindex[i])
            )
        elif i == 1:
            sum += (
                variableindex[i]
                * modindex[i - 1]
                * pow(modindex[i - 1], -1, modindex[i])
            )
        else:
            sum += (
                variableindex[i]
                * modindex[i - 1]
                * pow(modindex[i - 1], -1, modindex[i])
            )
else:
    for i in range(congruences):
        if i == 0:
            sum += (
                variableindex[i]
                * modindex[i + 1]
                * modindex[i + 2]
                * pow(modindex[i + 1] * modindex[i + 2], -1, modindex[i])
            )
        elif i == 1:
            sum += (
                variableindex[i]
                * modindex[i - 1]
                * modindex[i + 1]
                * pow(modindex[i - 1] * modindex[i + 1], -1, modindex[i])
            )
        else:
            sum += (
                variableindex[i]
                * modindex[i - 2]
                * modindex[i - 1]
                * pow(modindex[i - 2] * modindex[i - 1], -1, modindex[i])
            )
x = sum % globalmod

print(f"X = {x}")
print(
    f"If this was a low exponent RSA attack, know that m = {round(croot(x))} (the cube root of X)"
)
