import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    """Save tasks to file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)


def add_task(tasks):
    """Add a new task."""
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print(f'Task "{task}" added!')


def view_tasks(tasks):
    """View all tasks."""
    if not tasks:
        print("No tasks found!")
        return

    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{index}. [{status}] {task['task']}")


def complete_task(tasks):
    """Mark a task as complete."""
    view_tasks(tasks)
    task_index = int(input("Enter the number of the task to mark as complete: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_tasks(tasks)
        print(f'Task "{tasks[task_index]["task"]}" marked as complete!')
    else:
        print("Invalid task number!")


def delete_task(tasks):
    """Delete a task."""
    view_tasks(tasks)
    task_index = int(input("Enter the number of the task to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        deleted_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f'Task "{deleted_task["task"]}" deleted!')
    else:
        print("Invalid task number!")


def main():
    """Main function."""
    tasks = load_tasks()

    while True:
        print("\nTo-Do List")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Complete a task")
        print("4. Delete a task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
