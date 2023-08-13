import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    try:
        password_length = int(input("Enter desired password length: "))
        if password_length <= 0:
            print("Password length must be a positive number.")
            return

        password = generate_password(password_length)
        print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
