def crt(flag="auto", variableindex=None, modindex=None):
    if flag == "manual":
        # Manual input
        congruences = 0
        variableindex = []
        modindex = []
        while congruences < 2:
            try:
                congruences = int(input("Number of congruences? (At least 2): "))
            except ValueError:
                print("Please enter a valid integer.")

        for i in range(congruences):
            variable = int(input(f"Give variable for congruence {i+1}: "))
            mod = int(input(f"Give mod for congruence {i+1}: "))
            variableindex.append(variable)
            modindex.append(mod)

    globalmod = 1
    for mod in modindex:
        globalmod *= mod
    result = 0
    for i in range(len(variableindex)):
        partial_mod = globalmod // modindex[i]
        inverse = pow(partial_mod, -1, modindex[i])
        result += variableindex[i] * partial_mod * inverse
    return result % globalmod


if __name__ == "__main__":
    result = crt("manual")
    print(f"The result is: {result}")
