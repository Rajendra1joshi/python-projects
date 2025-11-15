import os

# folder_name = "new"

# if not os.path.exists(folder_name):
#     print("Folder doesn't exist.")
# else:
#     os.rmdir(folder_name)

folder_name ="Day-4"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
else:
    print("Folder exists")