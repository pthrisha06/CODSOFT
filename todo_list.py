tasks = []

while True:

    print("\nTO-DO LIST")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Update task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available")
        else:
            task_no = int(input("Enter the task number to delete: "))
            if 1 <= task_no <= len(tasks):
                tasks.pop(task_no - 1)
                print("Task deleted successfully!")
            else:
                print("Invalid task number!")
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available")
        else:
            task_no = int(input("Enter task number to update: "))
            if 1 <= task_no <= len(tasks):
                new_task = input("Enter new task: ")
                tasks[task_no - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number!")
    elif choice == "5":
        print("Thank you for using To-Do List!")
        break
    else:
        print("Invalid choice!")
