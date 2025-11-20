import os
import csv 
import json


file = "student.csv"

with open(file,"r",) as f:
    reader = csv.DictReader(f)
    data = list(reader)
    # print(data)


dict1 ={'Name': "Krishna","Marks" : "22","Subject":"Science"}

data.append(dict1)

with open(file, "w",newline="") as  f:
    writer = csv.DictWriter(f,fieldnames=["Name","Marks","Subject"])
    writer.writeheader()
    writer.writerows(data)

with open("student.json","w") as f:
    json.dump(data,f, indent=4)
