import os
import shutil
import time

# Define the source and destination directories
source_dir = r"C:\Users\Public\Documents\1ststep"
destination_dir = r"C:\Users\Public\Documents\Waves"

os.makedirs(destination_dir, exist_ok=True) #this should create the directory if it doesn't exist

def copy_files():
    while True:
        # List all files in the source directory
        files = os.listdir(source_dir)
        
        for file_name in files:
            # Get the full file path
            source_file = os.path.join(source_dir, file_name)
            destination_file = os.path.join(destination_dir, file_name)
            
            # Check if the file is a file (not a directory)
            if os.path.isfile(source_file):
                # Copy the file to the destination directory
                shutil.copy2(source_file, destination_file)
                print(f"Copied: {file_name}")
        
        # Wait for a short period before checking again
        time.sleep(10)

if __name__ == "__main__":
    copy_files()
