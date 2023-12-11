from menu import show_menu, process_choice
from task_handler import add_task, view_tasks, remove_task, save_tasks, load_tasks


def main():
    tasks = load_tasks()  # Load tasks from a file

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        try:
            process_choice(choice, tasks)
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
