import os
import csv

folder = 'report'

if not os.path.exists(folder):
    os.mkdir(folder)

with open("students.csv",'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row['Name']
        mark = row['Marks']
        subject = row['Subject']

        file_path = os.path.join(folder,f'{name}_report.txt')

        with open(file_path, "w") as f:
            f.write(f'Student name: {name} \n')   
            f.write(f'Marks: {mark}\n')
            f.write(f'Subject: {subject} \n')
            f.write(f"Status: {'PASS'if int(mark)> 40 else 'FAIL'}")