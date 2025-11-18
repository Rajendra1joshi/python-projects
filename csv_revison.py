import csv

# Reading csv file

# with open("friends.csv","r") as file:
#     data = csv.DictReader(file)
#     for row in data:
#         print(row["Name"])

# writing csv with dictwriter

# with open("New.csv","w", newline="") as file:
#     column_name = ["Name","Age"]
#     writer = csv.DictWriter(file, column_name)

#     writer.writeheader()
#     writer.writerow({"Name": "Sita","Age": "21"})

# with open("New.csv","r") as file:
#     data = csv.DictReader(file)
#     for row in data:
#         print(row)

#  /// CSV ALWAYS RETURNS STRING, SO DURING COMPARISON ALWAYS CONVERT IT INTO INTERGER
# FOR EXAMPLE

# with open("friends.csv","r") as f:
#     reader = csv.DictReader(f)

#     for row in reader:
#         if int(row['Age']) > 20 : //in this we change into int for comparison
#             print(row['Name'])

#   DONT WRITE writeheade() AGAIN INSIDE LOOPS
# 
