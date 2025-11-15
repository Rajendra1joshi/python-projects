import csv

# with open("friends.csv","r") as file:
#     read = csv.reader(file)

#     for row in read:
#         print("Name:", row[0])

# with open("friends.csv","r") as file:

#     read = csv.DictReader(file)

#     for row in read:
#         print(f"{row['Name']} is {row['Age']} years old.")

# count = 0 

# with open("friends.csv","r") as file:
#     reader = csv.DictReader(file)

#     for rows in reader:
#         if rows['Country'] == "Nepal":
#             count += 1

# print("Number of people from Nepal are: ",count)

# Creating a CSV file and importing data from here

with open("try.csv", "w",newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name","Roll"])
    writer.writerow(["Alex",'3'])