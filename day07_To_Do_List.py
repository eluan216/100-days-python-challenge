tasks = []

def show_tasks():
    if not tasks:
        print("\nYou have no tasks in your to-do list.")
        return
    
    print("\n===== YOUR TO-DO LIST =====")

    print("Tasks:")
    for number, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{number}. {task['task']} - {status}")

def add_task():
    name = input("\nEnter the task name: ").strip()

    if name:
        tasks.append({"task": name, "done": False})
        print(f"Task '{name}' added to your to-do list.")
    else:
        print("Task name cannot be empty. Please try again.")

def complete_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("\nEnter the task number to mark as done: "))
        if 1 <= number <= len(tasks):
            tasks[number - 1]["done"] = True
            print(f"Task '{tasks[number - 1]['task']}' marked as done.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Please enter a valid task number.")

def delete_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("\nEnter the task number to delete: "))
        if 1 <= number <= len(tasks):
            removed_task = tasks.pop(number - 1)
            print(f"Task '{removed_task['task']}' deleted from your to-do list.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Please enter a valid task number.")

while True:
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Thank you for using the To-Do List Manager!")
        break
    else:
        print("Invalid choice. Please try again. Choose a number between 1 and 5.")