import random
import string

def generate_password(length=12, include_uppercase=True, include_digits=True, include_special_chars=True):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if length < 1:
        raise ValueError("Password length should be at least 1 character.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage:
password = generate_password()
print("Generated Password:", password)
