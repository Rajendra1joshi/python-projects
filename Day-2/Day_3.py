import os

# path = r"C:\Users\N I T R O V15\Desktop"
# file = os.listdir(path)
# print(file)

folder_name = "new"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Created Successfully.")
else:
    print("Folder already exists.")