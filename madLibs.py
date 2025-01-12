import re

def mad_libs(input_file, output_file):
    # Open the input file and read its content
    with open(input_file, 'r') as file:
        content = file.read()
        
    # Define placeholders for the parts of speech
    placeholders = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
    
    # Use regex to find all placeholders in the content
    words = re.findall(r'\b(?:' + '|'.join(placeholders) + r')\b', content)

    # Replace each placeholder with user input
    for word in words:
        replacement = input(f"Enter a {word.lower()}:\n")  # Prompt user for input
        content = content.replace(word, replacement, 1)  # Replace only the first occurrence

    # Print the final result to the screen
    print("\nModified Text:")
    print(content)

    # Save the modified contentto the output file
    with open(output_file, 'w') as file:
        file.write(content)

    print(f"\nThe modified text has been saved to '{output_file}'.")

# Main program execution
def main():
    # Input and output file names
    input_file = 'madlibs_input.txt'  # Replace with your input file name
    output_file = 'madlibs_output.txt'  # Output file name

    try:
        mad_libs(input_file, output_file)
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
