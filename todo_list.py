todo_list = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as completed")
    print("4. Edit task")
    print("5. Delete task")
    print("6. Exit")

def view_tasks():
    if not todo_list:
        print("No tasks found.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list):
            status = "✅" if task["done"] else "❌"
            print(f"{i + 1}. {task['text']} [{status}]")

def add_task():
    task_text = input("Enter task: ")
    todo_list.append({"text": task_text, "done": False})
    print("Task added!")

def complete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= index < len(todo_list):
            todo_list[index]["done"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def edit_task():
    view_tasks()
    try:
        index = int(input("Enter task number to edit: ")) - 1
        if 0 <= index < len(todo_list):
            new_text = input("Enter new task text: ")
            todo_list[index]["text"] = new_text
            print("Task updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(todo_list):
            removed = todo_list.pop(index)
            print(f"Deleted task: {removed['text']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        edit_task()
    elif choice == "5":
        delete_task()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose between 1-6.")
