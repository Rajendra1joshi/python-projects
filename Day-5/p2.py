import os
import csv

with open('friends.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)


unique_data = [] #to store unique data
seen = set() #Set doesn't store duplicate data

for row in data:
    row_tuple = tuple(row.values()) #convert dict into tuple to perform the operation 

    if row_tuple not in seen: # row set ma xa vaney ignora garxa natra add garne
        seen.add(row_tuple)
        unique_data.append(row) # clean list ma add garxa
    
with open("Clean.csv",'w', newline='') as file:
    writer = csv.DictWriter(file,fieldnames=unique_data[0].keys()) # fieldnames = ['Name','Age','Country'] we can add maually
    # 1st row ko keys haru linxa dict ma ('key':'values') hunxa
    writer.writeheader() #write column names
    writer.writerows(unique_data) #write all rows

print(f'Cleaning complete! Total unique products: {len(unique_data)}')
