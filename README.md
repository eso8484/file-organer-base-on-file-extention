# File Organizer Script

This Python script automatically organizes files in a specified directory by moving them into subfolders based on their file extensions.

## Features
- Sorts files into folders based on their extensions (e.g., `PDF`, `JPG`, `TXT`).
- Automatically creates new folders if they don’t exist.
- Skips directories to avoid moving folders.
- Moves files with no extensions into an "Other" folder.

## Requirements
- Python 3.x installed on your system.
- The `os` and `shutil` modules (included in Python by default).

## Installation
1. Download and install [Python](https://www.python.org/downloads/) if you haven’t already.
2. Copy the script and save it as `organize_files.py`.

## Usage
1. Open the script in a text editor.
2. Modify the directory path in the script:
   ```python
   directory = "C:/Users/YourUsername/Downloads"
   ```
   Replace it with the folder path where you want to organize files.
3. Save the script.
4. Open **Command Prompt** (Windows) or **Terminal** (macOS/Linux).
5. Navigate to the script’s location using `cd`:
   ```sh
   cd path/to/script/folder
   ```
6. Run the script with:
   ```sh
   python organize_files.py
   ```
   (Use `python3` instead of `python` on macOS/Linux.)

## Example
### **Before Running the Script**
```
Downloads/
    file1.pdf
    file2.jpg
    file3.txt
    file4.docx
```
### **After Running the Script**
```
Downloads/
    PDF/
        file1.pdf
    JPG/
        file2.jpg
    TXT/
        file3.txt
    DOCX/
        file4.docx
```

## Customization
- You can modify the script to organize files based on **date created**, **size**, or **custom rules**.
- If you need additional features, edit the script accordingly.

## License
This script is open-source and free to use.

## Support
If you encounter any issues or need modifications, feel free to ask!


