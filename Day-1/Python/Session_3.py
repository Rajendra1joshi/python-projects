from datetime import datetime

def menu():
    print("\n=====Personal Diary====")
    print("1. Write a new diary entry.")
    print("2. Read all entries.")
    print("3. Exit  \n")


run = True
while run:
    menu()
    try:
        user = int(input("\nMake your Choice (1-3) : "))
    except ValueError:
        print("Only Choose betwee 1 and 3.😤")
        continue

    if user == 1:

        with open("diary.txt","a") as file:
            file.write(f"\n==== {datetime.now().strftime('%Y-%m-%d %H:%M')} ====\n")
            while True:
                entry = input("\n> ")

                if entry.lower() == "done":
                    print("✅Successfully Added.")
                    break
                else:
                    file.write(entry +'\n')
        
    elif user == 2:

        try:
            with open('diary.txt','r') as file:
                line = file.read().strip()
                if line:
                        print("======Your Entries Are:======")
                        print(line, end='')
                else:
                        print("No entries yet.")

        except FileNotFoundError:
            print("File doesn't exist.")

    elif user == 3:
        print("Good Byee.🙋‍♂️")
        run = False

    