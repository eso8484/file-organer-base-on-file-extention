#!/usr/bin/env python3
import os
import shutil
import sys

# Check if a directory is provided as a command-line argument
if len(sys.argv) > 1:
    source_dir = sys.argv[1]  # Use the provided directory
else:
    source_dir = os.getcwd()  # Default directory if none provided

# Verify the directory exists
if not os.path.isdir(source_dir):
    print(f"Error: Directory '{source_dir}' does not exist.")
    sys.exit(1)

# Dictionary of file extensions and their target folders
file_types = {
    # Documents
    ".txt": "TextFiles",
    ".doc": "Documents",
    ".docx": "Documents",
    ".pdf": "Documents",
    ".rtf": "Documents",
    ".odt": "Documents",
    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".csv": "DataFiles",
    ".ppt": "Presentations",
    ".pptx": "Presentations",
    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".tiff": "Images",
    ".tif": "Images",
    ".webp": "Images",
    ".svg": "Images",
    # Videos
    ".mp4": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",
    ".wmv": "Videos",
    ".flv": "Videos",
    ".webm": "Videos",
    ".mpeg": "Videos",
    ".mpg": "Videos",
    ".3gp": "Videos",
    # Audio
    ".mp3": "Audio",
    ".wav": "Audio",
    ".flac": "Audio",
    ".aac": "Audio",
    ".ogg": "Audio",
    ".wma": "Audio",
    ".m4a": "Audio",
    # Scripts and Code
    ".py": "Scripts",
    ".js": "Scripts",
    ".html": "WebFiles",
    ".htm": "WebFiles",
    ".css": "WebFiles",
    ".php": "Scripts",
    ".sh": "Scripts",
    ".bat": "Scripts",
    ".cpp": "Code",
    ".c": "Code",
    ".h": "Code",
    ".java": "Code",
    # Archives
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    ".tar.gz": "Archives",
    ".iso": "Archives",
    # Executables
    ".exe": "Executables",
    ".msi": "Executables",
    ".app": "Executables",
    ".dll": "Executables",
    # Miscellaneous
    ".log": "Logs",
    ".ini": "ConfigFiles",
    ".json": "DataFiles",
    ".xml": "DataFiles",
    ".md": "TextFiles",
    ".torrent": "Torrents"
}


other_folder = "Others"

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
        else:
            targetFolder = os.path.join(source_dir, other_folder)
            os.makedirs(targetFolder, exist_ok = True)
            shutil.move(file_path, os.path.join(targetFolder, filename))
            print(f"Moved {filename} to {targetFolder}")
    else:
        print(f"Skipped {filename} - Not a file")
