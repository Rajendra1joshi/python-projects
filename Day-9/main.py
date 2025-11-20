"""
Today i am learning:

1️⃣ os.walk() — walking through all folders
2️⃣ Searching for files automatically
3️⃣ Copying multiple files with conditions
4️⃣ Mini project: Find and copy all images from a big folder into one folder

"""

# see all folders + file of a certain location.

import os
from pathlib import Path

TARGET = Path(r"C:\Users\RajendraPrasadJoshi\Downloads")

for root, dirs, files in os.walk(TARGET):
    print("current folders: ", root)
    print("Sub-folders:", dirs)
    print(files)
    print("-" * 29)