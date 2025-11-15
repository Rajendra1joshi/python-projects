import os
import csv


# we can loop through multiple times by conveting the data into list
with open('friends.csv','r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

    print (data)

    for row in reader:
        row['Age'] = str(int(row['Age'])+2)
        print(row['Age'])