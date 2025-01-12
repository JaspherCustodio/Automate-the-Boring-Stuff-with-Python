import os
import re

def fill_in_gaps(folder, prefix):
    # Regular expression to match files like spam001.txt, spam002.txt, etc.
    pattern = re.compile(rf"^{re.escape(prefix)}(\d+)\.txt$")

    # Create a sorted list of matching files
    files = sorted(
        [f for f in os.listdir(folder) if pattern.match(f)],
        key=lambda x: int(pattern.match(x).group(1)) # Sort by number in filename
    )

    # Find the gaps in the numbering
    existing_numbers = set()
    for file in files:
        match = pattern.match(file)
        if match:
            existing_numbers.add(int(match.group(1)))

    next_number = 1 # Start checking from the first file number
    for file in files:
        match = pattern.match(file)
        if match:
            number = int(match.group(1))
            # If there's a gap, rename the later files
            if number > next_number:
                # Rename files to close the gap
                for i in range(number, next_number, -1):
                    old_name = f"{prefix}{i}.txt"
                    new_name = f"{prefix}{i + 1}.txt"
                    old_path = os.path.join(folder, old_name)
                    new_path = os.path.join(folder, new_name)
                    if os.path.exists(old_path, new_path):
                        os.rename(old_path, new_path)
                print(f"Renamed {old_name} to {new_name}")
            next_number = number + 1

# Example usage:
folder_to_search = r"C:\Users\YourUsername\Documents" # Replace with your folder
prefix = "spam"
fill_in_gaps(folder_to_search, prefix)
