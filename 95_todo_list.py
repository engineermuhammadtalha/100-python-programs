# To-Do List

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\n--- Your To-Do List ---")
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {status} {task['name']}")
        print()

while True:
    print("1. Add task")
    print("2. Mark task as done")
    print("3. Delete task")
    print("4. View tasks")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task_name = input("Enter task: ")
        tasks.append({"name": task_name, "done": False})
        print(f"'{task_name}' added!")
    elif choice == "2":
        show_tasks()
        num = int(input("Enter task number to mark done: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid number.")
    elif choice == "3":
        show_tasks()
        num = int(input("Enter task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            removed = tasks.pop(num)
            print(f"'{removed['name']}' deleted!")
        else:
            print("Invalid number.")
    elif choice == "4":
        show_tasks()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
