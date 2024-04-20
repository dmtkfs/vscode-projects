import sympy

n = int(input("Give N (must be prime): "))
phin = int(input("Give Φ(N): "))

x = sympy.symbols("x")
quadratic = sympy.Eq(x**2 - (n - phin + 1) * x + n, 0)
factors = sympy.solve(quadratic, x)

all_integers = all(factor.is_integer for factor in factors)

if all_integers:
    print("Factorization Complete: The factors [p, q] of N =", factors)
else:
    print("Factorization Failed. Not all factors were integers.")
