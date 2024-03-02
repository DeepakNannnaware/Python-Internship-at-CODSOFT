import random
import string

def generate_password(length=12, uppercase=True, lowercase=True, digits=True, special_chars=True):
    """Generate a random password."""
    if not any([uppercase, lowercase, digits, special_chars]):
        raise ValueError("At least one character type must be selected.")

    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if len(characters) == 0:
        raise ValueError("No characters available for generating password.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to Password Generator!")
    try:
        length = int(input("Enter the length of the password: "))
        uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
        digits = input("Include digits? (yes/no): ").lower() == 'yes'
        special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

        password = generate_password(length, uppercase, lowercase, digits, special_chars)
        print("Generated Password:", password)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
