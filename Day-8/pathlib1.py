from pathlib import Path

# pathlib (modern file paths) -> helps to work with file paths and folder easily.

p = Path(r"C:\Users\N I T R O V15\Desktop\Programming\python\New.csv")
print(p)

print(p.exists())

print(p.is_file())
print(p.is_dir())

file = Path("first_json.json")

print(file.stem) #PRINT ONLY THE NAME OF THE FILE NOT EXTENSION

print(file.suffix)

#   JOIN PATH EASILY
# old_path = Path("")
# new_path = old_path / "file.txt"

# Loop through the files in a folder

q = Path(r"C:\Users\N I T R O V15\Desktop\Programming\python\Week-1")

for item in q.iterdir():
    print(item)

# FIND OLNY CERTAIN FILE TYPES

for file in q.glob("*.py"):
    print(file)

# CREATES THE FOLDER AND CHECKS IF IT EXISTS IN A SAME LINE

Path("myfiles").mkdir(exist_ok = True)