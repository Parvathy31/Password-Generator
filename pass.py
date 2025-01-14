import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # Build the character pool
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    # Initialize password components
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    # Generate the password
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        # Check for numbers and special characters
        if new_char in digits:
            has_number = True
        if new_char in special:
            has_special = True

        # Validate criteria
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

# Generate and print a password
pwd = generate_password(10)
print(pwd)
