import random
import string

def generate_password(length):
    # Define the character set to use for generating the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password using the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        try:
            # Prompt the user for the desired password length
            length = int(input("Enter the desired length for your password (minimum 6): "))
            if length < 6:
                print("Password length should be at least 6.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    # Generate and display the password
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
