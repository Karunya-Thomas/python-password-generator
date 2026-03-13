def load_tasks():
    try:
        with open("tasks.txt","r")as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return[]

def save_tasks(tasks):
    with open("tasks.txt","w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    task = input("Enter new task:")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

def view_tasks(tasks):
    print("\n Your Tasks:")
    if not tasks:
        print("No Tasks Available")
    else: 
        for i, task in enumerate(tasks):
            print(i+1,"-",task)

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter task number to delete: "))
        if 0 < task_number <= len(tasks):
            tasks.pop(task_number - 1)
            save_tasks(tasks)
            print("Task Deleted!")
        else:
            print("Invalid Task Number")
    except ValueError:
        print("Please Enter a valid number")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            delete_task(tasks)

        elif choice == "4":
            print("Good Bye")
            break

        else:
            print("Invalid choice")


main()