import os
import csv 
import json


file = "student.csv"

with open(file,"r",) as f:
    reader = csv.DictReader(f)
    data = list(reader)
    # print(data)

    for row in reader:
        print(row)
dict1 ={'Name': "Krishna","Marks" : "22","Subject":"Science"}

data.append(dict1)

with open(file, "w") as  f:
    writer = csv.DictWriter(f,fieldnames=["Name","Marks","Subject"])
    writer.writeheader
    writer.writerows(data)
