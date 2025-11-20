import os

# os module


# ---- check current working directory ----
print(os.getcwd()) 


# ---- change directory ----
# os.chdir(r"C:\Users\N I T R O V15\Desktop\Programming\python\Day-8") 


# ---- list files in folder ----
# file = os.listdir()
# print(file)


# ---- check if file/folder exists ----
# if os.path.exists("Day-8"):
#     print("Exists")
# else:
#     print("Doesn't exists.")


# ---- Make folder ----
# os.mkdir("New folder") #single folder 
# os.makedirs("data/2025/janaury") # mulitple folders inside


# ---- Deleting file/folder ----
# os.remove("file_name")
# os.rmdir("empty_folder")


# ---- rename file ----
# os.rename("old_name","new_name")