import os
import shutil

# Set the directory to organize
source_dir = "C:/Users/YourUsername/Downloads"

# Dictionary of file extensions and their target folders
file_types = {
    ".txt": "TextFiles",
    ".jpg": "Images",
    ".png": "Images",
    ".pdf": "Documents",
    ".py": "Scripts"
}

# Create folders and move files
for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)
    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1].lower()
        if extension in file_types:
            target_folder = os.path.join(source_dir, file_types[extension])
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, filename))
            print(f"Moved {filename} to {file_types[extension]}")
