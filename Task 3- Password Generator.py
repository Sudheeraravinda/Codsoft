import random
import string

# Global strings to be used to randomly generate password components
string_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string_num = '0123456789'
string_special = '~!@#$%^&*()'

# Solution as follows
def generate_password(length, use_special_chars, use_numbers):
    """Generates a random password based on user preferences."""
    password = ''

    # Generate remaining characters
    for _ in range(length-2):
        password += random.choice(string_char)

    # Replace second last character with number if required
    if use_numbers:
        password = password + random.choice(string_num)
    else:
        password = password + random.choice(string_char)

    # Replace last character with special character if required
    if use_special_chars:
        password = password + random.choice(string_special)
    else:
        password = password + random.choice(string_char)

    return password


# Solution as follows
length = int(input("Enter the length of the password: "))
use_special_chars = input("Do you want to include special characters? (yes/no): ").lower() == 'yes'
use_numbers = input("Do you want to include numbers? (yes/no): ").lower() == 'yes'


# Generate and print the password
generated_password = generate_password(length, use_special_chars, use_numbers)
print("\n")
print("Generated Password:", generated_password)