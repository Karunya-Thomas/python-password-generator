tasks = []
# Load tasks from a file 

try: 
    with open("tasks.txt","r") as file:
        tasks = file.read().splitlines()
except FileNotFoundError:
    pass

while True:
    print("\nTo-Do Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your Choice :").strip()

    if choice == "1":
        task = input("Enter a new task : ")
        tasks.append(task)

        with open("tasks.txt","a")as file:
            file.write(task + "\n")
        print("Task Added!")

    elif choice == "2":
        print("\n Your Tasks:")
        if not tasks:
            print("Not tasks available.")
        else:
            for i, task in enumerate(tasks):
                print(i + 1, "-", task)

    elif choice == "3":
        task_number = int(input("Enter task number to delete:"))

        if 0 < task_number <= len(tasks):
            tasks.pop(task_number - 1)

        with open("tasks.txt","w")as file:
            for task in tasks:
                file.write(task + "\n")
        print("Task Deleted!")

    elif choice == "4":
        print("GoodBye!")
        break
    
    else:
        print("Invalid Choiice!")