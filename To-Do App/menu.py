from task_handler import add_task, view_tasks, remove_task, save_tasks


def show_menu():
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Save Tasks")
    print("5. Quit")


def process_choice(choice, tasks):
    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        remove_task(tasks)
    elif choice == "4":
        save_tasks(tasks)
    elif choice == "5":
        save_tasks(tasks)  # Save tasks before quitting
        print("Exiting Task Manager.")
        exit()
    else:
        raise ValueError("Invalid choice. Please enter a number between 1 and 5.")