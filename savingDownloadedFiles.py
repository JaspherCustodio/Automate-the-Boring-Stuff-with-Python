import os
import shutil

def selective_copy(source_folder, target_folder, file_extensions):
    # Ensure target folder exists
    os.makedirs(target_folder, exist_ok=True)

    # Walk through folder tree
    for foldername, subfolders, os.walk(source_folder):
        for filename in filenames:
            # Check if the file has specified extension
            if filename.lower().endswith(tuple(file_extensions)):
                # Get full path of the source file
                source_path = os.path.join(foldername, filename)

                # Define destination path
                destination_path = os.path.join(target_folder, filename)

                # Copy the file to the target folder
                shutil.copy2(source_path, destination_path)
                print(f"Copied: {source_path} -> {destination_path}")

    print("\nSelective copy complete!")

# Example usage:
source_folder = r"C:Users\YourUsername\Documents"  # Replace with your source folder path
target_folder = r"C:\Users\Username\SelectiveCopies"  # Replace with your target folder path
file_extensions = ['.pdf', '.jpg']  # Specify extensions you want to copy

selective_copy(source_folder, target_folder, file_extensions)
