import os

folder_name = "Day-1"

files = os.listdir(folder_name)

for count, filename in enumerate(files, start=1):

    old_path = os.path.join(folder_name,filename)

    if os.path.isfile(old_path):
        name,ext = os.path.splitext(filename)

        new_name = f"Session_{count}{ext}"

        new_path = os.path.join(folder_name,new_name)

        os.rename(old_path,new_path)
        