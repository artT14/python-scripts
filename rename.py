# Takes a directory of files and renames it based on the given naming convention below
import os

def rename_files():
    # Get list of all files in the current directory
    dir_path = '.'
    files = [f for f in os.listdir(dir_path) if os.path.isfile(f)]
    print(files)
    # Sort files alphabetically for a consistent order
    files.sort()
    
    # Loop through each file and rename
    for i, filename in enumerate(files, 1):
        # Construct new filename
        # Assuming the extension needs to be preserved
        file_extension = os.path.splitext(filename)[1]
        new_filename = f"mask{i}{file_extension}"
        
        # Rename the file
        os.rename(filename, new_filename)
        print(f"Renamed {filename} to {new_filename}")

if __name__ == "__main__":
    rename_files()
