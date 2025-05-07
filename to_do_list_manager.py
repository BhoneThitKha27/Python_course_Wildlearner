# Step 1: Initialize the empty to-do list
todo_list = []

# Step 2: Show menu and loop
while True:
    print("\n--- To-Do List Manager ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        if not todo_list:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        new_task = input("Enter the task: ")
        todo_list.append(new_task)
        print("Task added!")

    elif choice == "3":
        if not todo_list:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter the task number to remove: "))
                if 1 <= task_num <= len(todo_list):
                    removed = todo_list.pop(task_num - 1)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")