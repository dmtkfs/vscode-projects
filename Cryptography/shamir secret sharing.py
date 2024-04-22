from tools.generators import generate_polynomial_for_secret as generate_polynomial
from tools.checkers import check_isprime as isprime


def input_shares(min_threshold):
    shares = []
    print(
        f"Enter at least {min_threshold} shares in the format (x, y), or type 'no' to stop once the minimum is met."
    )
    while True:
        if len(shares) >= min_threshold:
            prompt = f"At least {min_threshold} shares entered. Enter more shares or type 'no' to finish: "
        else:
            prompt = f"Enter share {len(shares) + 1} (required {min_threshold}): "

        share_input = input(prompt)
        if share_input.lower() == "no":
            if len(shares) >= min_threshold:
                return shares, True
            else:
                print(f"Not enough shares, give more to reach {min_threshold}. ")
                continue

        try:
            x, y = map(int, share_input.split(","))
            shares.append((x, y))
        except ValueError:
            print("Invalid format. Try again like this (x,y): ")


def evaluate_polynomial(coefficients, x, p):
    result = 0
    for coefficient in reversed(coefficients):
        result = (result * x + coefficient) % p
    return result


def reconstruct_secret(shares, p):
    k = len(shares)
    secret = 0
    for j in range(k):
        xj, yj = shares[j]
        lj = 1
        for m in range(k):
            if m != j:
                xm, _ = shares[m]
                lj *= (xm * pow(xm - xj, -1, p)) % p
        term = (yj * lj) % p
        secret = (secret + term) % p
    return secret


user_choice = input("Will you give the share tuples? (yes/no): ")
if user_choice.lower() == "yes":
    k = int(
        input(
            "Enter the threshold (minimum number of shares needed to reconstruct the secret): "
        )
    )
    shares, shares_inputted = input_shares(k)
    if shares:
        p = int(input("Enter the prime number used in share generation: "))
        original_secret = reconstruct_secret(shares, p)
        print("Reconstructed Secret:", original_secret)
    else:
        print("No shares were entered.")
else:
    secret = int(input("Enter the secret: "))
    m = int(input("Give the number of shares to generate: "))
    k = int(input("Give the threshold (degree of polynomial + 1): "))
    p = int(
        input(
            f"Give a prime number p larger than the secret {secret} and the number of shares {m}: "
        )
    )
    while not isprime(p):
        p = int(input("p not prime. Try again: "))
    coefficients = generate_polynomial(secret, k, p)
    shares = [(i, evaluate_polynomial(coefficients, i, p)) for i in range(1, m + 1)]
    print("Shares generated: ")
    for share in shares:
        print(f"Share {share[0]}: {share[1]}")
    original_secret = reconstruct_secret(shares, p)
    print("Reconstructed Secret:", original_secret)
