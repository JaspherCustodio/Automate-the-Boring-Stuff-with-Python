import re

def is_strong_password(password):
    #Check for minimum length
    if len(password) < 8:
        return False
    
    # Check for at least one uppercase letter, one lowercase letter, and one digit
    if not re.search(r'[A-Z]', password):  # At least one Uppercase letter
        return False
    if not re.search(r'[a-z]', password):  # At least one lowercase letter
        return False
    if not re.search(r'[0-9]', password):  # At least one digit
        return False

    # If all conditions are met, the password is strong
    return True

while True:
    user_input = input("Enter password: ")
    if is_strong_password(user_input):
        print(f"Password '{user_input}' is strong.\n")
        print("Logging in...")
        break
    else:
        print(f"Password '{user_input}' is weak, try again.\n")
        print("Use at least 8 characters one uppercase letter one \
            \nlowercase letter and one number in your password\n")
