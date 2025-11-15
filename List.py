Task = [] 
while True:
    print("\n To do list")
    print("1. Add a task")
    print("2. View Tasks")
    print("3. Remove a task")
    print("4. Exit")
    choice = int(input("Choose an option from 1 to 4: "))
    if choice == 1:
        for i in Task:
            task = input("Enter the task to add: ")
            Task.append(task)
            print(f"task {task} added")
    elif choice == 2:
        for i in Task:
            print(i)
    elif choice == 3:
        task = input("Enter the task to delete")
        Task.remove(task)
        print(f"task {task} deleted")
    elif choice == 4:
        print("Thanks for using the to-do list, Goodbye")
        break
     
