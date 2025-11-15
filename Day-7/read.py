import json

#to read json file through python

with open('first_json.json','r') as file:
    read = json.load(file)

print(read) #printing after the opening is recommanded though inside is also correct.

