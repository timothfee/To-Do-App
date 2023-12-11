import datetime


def add_task(tasks):
    task_name = input("Enter task name: ")
    due_date_str = input("Enter due date (YYYY-MM-DD): ")

    try:
        due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

    priority = input("Enter priority level: ")

    task = {
        "name": task_name,
        "due_date": due_date,
        "priority": priority
    }

    tasks.append(task)
    print(f"Task '{task_name}' added successfully.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['name']} (Due: {task['due_date']}, Priority: {task['priority']})")


def remove_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the number of the task to remove: ")) - 1
        removed_task = tasks.pop(index)
        print(f"Task '{removed_task['name']}' removed successfully.")
    except (ValueError, IndexError):
        raise ValueError("Invalid task number.")


def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['name']},{task['due_date']},{task['priority']}\n")


def load_tasks():
    tasks = []
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task_data = line.strip().split(",")
                task = {
                    "name": task_data[0],
                    "due_date": datetime.datetime.strptime(task_data[1], "%Y-%m-%d").date(),
                    "priority": task_data[2]
                }
                tasks.append(task)
    except FileNotFoundError:
        pass  # Ignore if the file doesn't exist

    return tasks
