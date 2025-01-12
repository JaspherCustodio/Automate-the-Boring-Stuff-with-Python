import os
import re

def insert_gap(folder, prefix, gap_position):
    # Regular expression to match files like spam001.txt, spam002.txt, etc.
    pattern = re.compile(rf"^{re.escape(prefix)}(\d+)\.txt$")

    # Create a sorted list of matching files
    files = sorted(
        [f for f in os.listdir(folder) if pattern.match(f)],
        key=lambda x: int(pattern.match(x).group(1)) # Sort by number in filename
    )

    # Insert gap by renaming files starting from the gap_position
    for files in files:
        match = pattern.match(file)
        if match:
            number = int(match.group(1))
            if number >= gap_position:
                # Rename file to insert the gap
                old_name = file
                new_name = f"{prefix}{number + 1:03d}.txt" # Increase number by 1
                old_path = os.path.join(folder, old_name)
                new_path = os.path.join(folder, new_name)
                os.rename(old_path, new_path)
                print(f"Renamed {old_name} to {new_name}")

    # Create a new file at the gap position
    new_gap_filename = f"{prefix}{gap_position:03d}.txt"
    new_gap_path = os.path.join(folder, new_gap_filename)
    with open(new_gap_path, 'w') as f:
        f.write(f"New file to fill the gap {gap_position}\n")
    print(f"Created new file: {new_gap_filename}")

# Example usage:
folder_to_search = r"C:\Users\YourUsername\Documents" # Replace with your folder
prefix = "spam"
gap_position = 3 # The position where you want to insert the gap
insert_gap(folder_to_search, prefix, gap_position)
