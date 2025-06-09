#!/usr/bin/env python3

import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

# Define file types
file_types = {
    ".txt": "TextFiles", ".md": "TextFiles",
    ".doc": "Documents", ".docx": "Documents", ".pdf": "Documents", ".rtf": "Documents", ".odt": "Documents",
    ".xls": "Spreadsheets", ".xlsx": "Spreadsheets", ".csv": "DataFiles",
    ".ppt": "Presentations", ".pptx": "Presentations",
    ".jpg": "Images", ".jpeg": "Images", ".png": "Images", ".gif": "Images", ".bmp": "Images", ".tiff": "Images",
    ".tif": "Images", ".webp": "Images", ".svg": "Images",
    ".mp4": "Videos", ".avi": "Videos", ".mkv": "Videos", ".mov": "Videos", ".wmv": "Videos", ".flv": "Videos",
    ".webm": "Videos", ".mpeg": "Videos", ".mpg": "Videos", ".3gp": "Videos",
    ".mp3": "Audio", ".wav": "Audio", ".flac": "Audio", ".aac": "Audio", ".ogg": "Audio", ".wma": "Audio",
    ".m4a": "Audio",
    ".py": "Scripts", ".js": "Scripts", ".php": "Scripts", ".sh": "Scripts", ".bat": "Scripts",
    ".html": "WebFiles", ".htm": "WebFiles", ".css": "WebFiles",
    ".cpp": "Code", ".c": "Code", ".h": "Code", ".java": "Code",
    ".zip": "Archives", ".rar": "Archives", ".7z": "Archives", ".tar": "Archives",
    ".gz": "Archives", ".tar.gz": "Archives", ".iso": "Archives",
    ".exe": "Executables", ".msi": "Executables", ".app": "Executables", ".dll": "Executables",
    ".log": "Logs", ".ini": "ConfigFiles", ".json": "DataFiles", ".xml": "DataFiles",
    ".torrent": "Torrents"
}

other_folder = "Others"

def log(message):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")

class FileOrganizer(FileSystemEventHandler):
    def __init__(self, directory):
        self.directory = directory

    def on_modified(self, event):
        self.organize_files()

    def on_created(self, event):
        self.organize_files()

    def organize_files(self):
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)

            if not os.path.isfile(file_path) or filename.startswith("."):
                continue

            ext = os.path.splitext(filename)[1].lower()
            folder = file_types.get(ext, other_folder)
            target_dir = os.path.join(self.directory, folder)
            os.makedirs(target_dir, exist_ok=True)

            new_path = os.path.join(target_dir, filename)
            if os.path.exists(new_path):
                # Avoid overwrite by adding timestamp
                base, ext = os.path.splitext(filename)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                new_path = os.path.join(target_dir, f"{base}_{timestamp}{ext}")

            try:
                shutil.move(file_path, new_path)
                log(f"Moved '{filename}' to '{folder}'")
            except Exception as e:
                log(f"Failed to move '{filename}': {e}")

def main():
    source_dir = os.getcwd()
    log(f"Monitoring directory: {source_dir}")

    event_handler = FileOrganizer(source_dir)

    # Organize existing files immediately
    event_handler.organize_files()

    observer = Observer()
    observer.schedule(event_handler, path=source_dir, recursive=False)
    observer.start()

    try:
        while True:
            event_handler.organize_files()
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
        log("Stopped monitoring.")
    observer.join()

if __name__ == "__main__":
    main()
