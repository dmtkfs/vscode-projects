import re


def check_password_strength(password):
    errors = []

    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")

    if not re.search(r"[a-z]", password):
        errors.append("Password must contain at least one lowercase letter.")

    if not re.search(r"[A-Z]", password):
        errors.append("Password must contain at least one uppercase letter.")

    if not re.search(r"[0-9]", password):
        errors.append("Password must contain at least one digit.")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        errors.append(
            'Password must contain at least one special character (!@#$%^&*(),.?":{}|<>).'
        )

    if not errors:
        return "Password is strong."
    else:
        return "Password is weak: " + "; ".join(errors)


# Example usage
password = input("Enter your password: ")
result = check_password_strength(password)
print(result)
