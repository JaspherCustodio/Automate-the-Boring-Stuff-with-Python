import re

def regex_strip(text, chars=None):
    # If no specific characters are provided, strip whitespace by default.
    if chars is None:
        # Remove whitespace from start and end
        return re.sub(r'^\s+|\s$', '', text)
    else:
        # Create a regex pattern to match any of the specified characters
        pattern = f"^[{re.escape(chars)}]+|[{re.escape(chars)}]+$"
        # Remove the specified characters from start and end
        return re.sub(pattern, '', text)

while True:
    user_input = input("I will strip your input both sides: ")
    if regex_strip(user_input) == '':
        break

    char_input = input("Input character/s to strip(from start and end): ")
    if regex_strip(char_input) == '':
        print(regex_strip(user_input))
    else:
        print(regex_strip(user_input, char_input))
    print()
