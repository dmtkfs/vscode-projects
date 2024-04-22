def croot(n):
    return int(round(n ** (1 / 3))) if n >= 0 else -int(round((-n) ** (1 / 3)))


def sqrt_x_mod_n(x, n):
    return pow(x, (n + 1) // 4, n)
