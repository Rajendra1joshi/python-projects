import os 

folder_name = "test_folder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("✔️Successfully created")
else:
    print("❌FIle already exists.")

directory = "."
items = os.listdir(directory)
for item in items:
    if os.path.isfile(item):
        print(f"File: {item}")
    elif os.path.isdir(item):
        print(f"Folder: {item}")