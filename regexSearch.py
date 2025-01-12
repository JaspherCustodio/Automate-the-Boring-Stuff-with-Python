import os
import re

def regex_search(folder, pattern):
    try:
        # Compile the user-supplied regex pattern
        regex = re.compile(pattern)

        # List all .txt files in the specified folder
        txt_files = [f for f in os.listdir(folder) if f.endswith('.txt')]

        # Check if no text files are found
        if not txt_files:
            print("No .txt files found in the specified folder.")
            return

        print("\nSearching for matches...\n")

        # Loop through each .txt file
        for file_name in txt_files:
            file_path = os.path.join(folder, file_name)

            # Open and read each file line by line
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                lines = file.readlines()
                for line_num, line in enumerate(lines, 1):
                    # Search for pattern matches in each line
                    if regex.search(line):
                        print(f"[{file_name}: Line{line_num}] {line.strip()}")

        print("\nSearch completed.")
    except FileNotFoundError:
        print(f"Error: The folder '{folder}' was not found.")
    except re.error:
        print("Invalid regular expression pattern.")
    except Exception as e:
        print(f"An error occured: {e}")

# Main function
def main():
    # Prompt the user for input
    folder = input("Enter the folder path: ")
    pattern = input("Enter the regular expression: ")

    # Perform the regex search
    regex_search(folder, pattern)

if __name__ == "__main__":
    main()
