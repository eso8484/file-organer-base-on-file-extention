#!/usr/bin/env python3

import os
import shutil
import sys

if len(sys.argv) > 1:
    src_folder = sys.argv[1]
else:
    src_folder = os.getcwd()

if not os.path.isdir(src_folder):
    print(f" Error: The directory '{src_folder}' does not exist")
    sys.exit(1)

file_types = {
        ".txt": "Text Files",
        ".pdf": "PDF Documents"
        }
for filename in os.listdir(src_folder):

    file_path = os.path.join(src_folder, filename)

    if os.path.isfile(file_path):
        extention = os.path.splitext(filename)[1].lower()
        if extention in file_types:
            trg_folder = os.path.join(src_folder, file_types[extention])
            os.mkdirs(trg_folder, exist_ok = True)
            shutil.move(file_path, os.path.join(trg_folder, filename))
        else:
                print(f"skipped {filename}, not an extention")
    else:
                print(f"skippede {filename} ot in part")
