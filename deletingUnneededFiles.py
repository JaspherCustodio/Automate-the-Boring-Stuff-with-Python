import os

def find_large_files(folder, size_limit):
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            # Get the absolute path of the file
            file_path = os.path.join(foldername, filename)
            try:
                # Get the size of the file in bytes
                file_size = os.path.getsize(file_path)
                # Convert size limit to bytes (1 MB = 1,048,576 bytes)
                if file_size > size_limit:
                    size_mb = file_size / (1024 * 1024) # Convert to MB
                    print(f"{file_path} - {size_mb:.2f} MB")
            except FileNotFoundError:
                # Handle cases where files may be deleted/moved during the process
                print(f"Could not access {file_path}")
    print("\nSearch complete!")

# Example usage:
folder_to_search = r"C:\Users\YourUsername\Documents"  # Replace with your target folder
size_limit = 100 * 1024 * 1024  # 100MB in bytes

find_large_files(folder_to_search, size_limit)
