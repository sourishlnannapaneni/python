from datetime import datetime

def add_entry():
    entry = input("Enter your journal entry: ")
    with open("Journal.txt", "a") as file:
        date = datetime.now().strftime("%d/%m/%y %H:%M:%S:")
        file.write(date + " " + entry + "\n")
    print("entry saved")

def view_entry():
    with open("Journal.txt", "r") as file:
        print("\n Your Journal Entries: ")
        index = 1
        for i in file:
            print(f"{index}) {i.strip()}")
            index = index + 1
            
while True:
    print("\n Journal App ") 
    print("1. Add Entry")
    print("2. View Entry") 
    print("3. Exit")

    choice = int(input("Choose an option: "))
    if choice == 1: 
        add_entry()

    elif choice == 2:
        view_entry()

    elif choice == 3:
        print("Thanks for using the app!")
        break

    else:
        print("Invalid Choice, please make the correct one.")
