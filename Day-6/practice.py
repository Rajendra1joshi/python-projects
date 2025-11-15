import csv



with open('students','r') as file:
    reader = csv.DictReader(file)

    for row in reader:
