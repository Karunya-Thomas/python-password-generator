tasks = []
while True:
    print("\nTo-Do Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")    

    choice = input("Enter your Choice : ").strip()

    if choice == "1":
        task = input("Enter new task : ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        
        if len(tasks) == 0:
            print("No tasks available")

        for i, task in enumerate(tasks):
            print(i + 1, "-", task)

    elif choice == "3":
        task_number = int(input("Enter the task number to delete: "))
        if 0 < task_number <= len(tasks):
            tasks.pop(task_number - 1)
            print("Task Deleted!")

    elif choice == "4":
        print("Good Bye")
        break

    else:
        print("Invalid Choice")

