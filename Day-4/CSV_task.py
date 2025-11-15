import csv

count = 0

with open("students.csv","w", newline="") as file:
    write = csv.writer(file)

    write.writerow(['Name','Marks','Subject'])
    write.writerow(['Aayush','78','Math'])
    write.writerow(['Rita','88','Science'])
    write.writerow(['Nabin','65','English'])
    write.writerow(['Luna','92','Math'])
    write.writerow(['Raj','81','Science'])

with open("students.csv","r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(f"{row['Name']} likes {row['Subject']}.")
        if int(row['Marks']) >  80:
            count+= 1

print(f"Total students with marks above 80 : {count}")