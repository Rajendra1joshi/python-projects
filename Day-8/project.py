import os
import shutil
from pathlib import Path

TARGET = Path(r"C:\Users\N I T R O V15\Desktop\Programming\python")

CATEGORIES = {
    "Images": [".png", ".jpg", ".jpeg"],
    "Videos": [".mp4", ".mov", ".mkv"],
    "Text":   [".txt"],
    "CSV":    [".csv"],
    "Json":   [".json"]
}

log_file = TARGET / "log.txt"
   

# ====== LOGGING FUNCTION ======
def write_log(message):
    with open(log_file, "a") as log:
        log.write(message + "\n")
    print(message)


# ====== ORGANIZER FUNCTION ======
def organize_files():
    """
    Categories bata folder haru create garxa:
    Images, Videos, Text, CSV, Json etc.
    Ani tyo folder vitra respective file move garxa.
    """

    # Step 1: Create category folders
    for category in CATEGORIES:
        folder = TARGET / category
        folder.mkdir(exist_ok=True)

    # Step 2: Check every file in target folder
    for file in TARGET.iterdir():

        if file.is_dir():  
            continue

        extension = file.suffix.lower()
        moved = False

        # Step 3: Match extension to category
        for category, extensions in CATEGORIES.items():
            if extension in extensions:
                destination = TARGET / category / file.name
                shutil.move(str(file), str(destination))
                write_log(f"Moved: {file.name} -> {category}")
                moved = True
                break

        # Step 4: If no match found
        if not moved:
            write_log(f"Skipped (no category): {file.name}")


# ====== RUN SCRIPT ======
if __name__ == "__main__":
    write_log("=== Organizer Started ===")
    organize_files()
    write_log("=== Organizer Finished ===")
