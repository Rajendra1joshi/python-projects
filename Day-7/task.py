import json
count = 0
with open("students.json",'r') as file:
    data = json.load(file)

for student in data['students']:
    student['marks'] += 5

    if student['marks'] > 85:
        count += 1

with open('students_updated.json','w') as file:
    json.dump(data, file, indent=4)

print(f"Updated successfully! Total above 85: {count}")

