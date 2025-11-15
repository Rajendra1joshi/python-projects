import os 
import shutil

folder = "D:\\downloads"

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".txt", ".pdf", ".docx", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".flac"],
    "Compressed": [".zip", ".rar", ".7z"],
    "Programs": [".exe", ".msi"]

}

for filename in os.listdir(folder):

    source = os.path.join(folder,filename)

    if os.path.isfile(source):
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        moved = False

        for group, extensions in file_types.items():
            if ext in extensions :
                target_dir = os.path.join(folder, group) 
                os.makedirs(target_dir, exist_ok=True)
                shutil.move(source,os.path.join(target_dir,filename))
                moved = True
                break
        
        if not moved:
            others = os.path.join(folder,"others")
            os.makedirs(others, exist_ok=True)
            shutil.move(source, os.path.join(others,filename))
            