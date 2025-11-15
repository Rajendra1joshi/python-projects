import os
import csv
# what i learned till the date (day- 4)

# reading, writing, and appending file

# with open('new.txt','w') as file:
#     writer = file.write("Hello World")

# with open("new.txt","r") as file:
#     read = file.read()
#     print(read)

# CSV FILE

# with open("try.csv","r") as file:
#     reader = csv.DictReader(file) 

#     for row in reader:
#         print(row['Name'])

folder = "Day-5"

if not os.path.exists(folder):
    os.mkdir(folder)
else:
    print("Already Exists.")