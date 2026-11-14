
import secrets
import string


def generate_password(length, use_uppercase, use_lowercase,
                      use_numbers, use_symbols):

    characters = ""

    if use_uppercase:
        characters += string.ascii_uppercase

    if use_lowercase:
        characters += string.ascii_lowercase

    if use_numbers:
        characters += string.digits

    if use_symbols:
        characters += "!@#$%^&*()_+-=[]{}?"

    if not characters:
        return None

    # Ensure at least one character from every selected category
    password = []

    if use_uppercase:
        password.append(secrets.choice(string.ascii_uppercase))

    if use_lowercase:
        password.append(secrets.choice(string.ascii_lowercase))

    if use_numbers:
        password.append(secrets.choice(string.digits))

    if use_symbols:
        password.append(secrets.choice("!@#$%^&*()_+-=[]{}?"))

    # Fill the remaining length
    for _ in range(length - len(password)):
        password.append(secrets.choice(characters))

    # Shuffle the password
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


def check_password_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in "!@#$%^&*()_+-=[]{}?" for char in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"
