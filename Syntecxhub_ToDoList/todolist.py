from datetime import datetime
import json
import os
import winsound
import pandas as pd

FILE_NAME = "tasks.json"


def make_sound():
    winsound.Beep(600, 1500)


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return {}
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except Exception:
        print("Error loading file. Starting with empty tasks.")
        return {}


def save_tasks(tasks):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=4)
    except Exception:
        print("Error saving tasks.")


def add_task(tasks):
    name = input("Task name: ")
    if name in tasks:
        print("Task already exists.")
        return

    desc = input("Description: ")
    start = input("Start Date (YYYY-MM-DD HH:MM AM/PM): ")
    deadline = input("Deadline (YYYY-MM-DD HH:MM AM/PM): ")
    priority = input("Priority (High/Medium/Low): ").capitalize()

    tasks[name] = {
        "description": desc,
        "start_date": start,
        "deadline": deadline,
        "status": "Pending",
        "priority": priority
    }

    save_tasks(tasks)
    print("Task added successfully.")


def mark_done(tasks):
    name = input("Enter task name to mark completed: ")

    if name in tasks:
        tasks[name]["status"] = "Completed"
        save_tasks(tasks)
        make_sound()
        print("Task marked as completed.")
    else:
        print("Task not found.")


def delete_task(tasks):
    name = input("Enter task name to delete: ")

    if name in tasks:
        del tasks[name]
        save_tasks(tasks)
        print("Task deleted.")
    else:
        print("Task not found.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    df = pd.DataFrame(tasks).T
    print("\nTask List:")
    print(df)


def check_deadlines(tasks):
    now = datetime.now()

    for name, details in tasks.items():
        try:
            deadline = datetime.strptime(details["deadline"], "%Y-%m-%d %I:%M %p")
            if deadline < now and details["status"] == "Pending":
                print(f"⚠ Task Overdue: {name}")
        except:
            pass


def menu():
    print("\n===== TASK MANAGER =====")
    print("1. Add Task")
    print("2. Mark Task Completed")
    print("3. View Tasks")
    print("4. Delete Task")
    print("5. Exit")

if __name__ == "__main__":
    tasks = load_tasks()

    while True:
        check_deadlines(tasks)
        menu()

        choice = input("Enter choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            mark_done(tasks)

        elif choice == "3":
            view_tasks(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Exiting Task Manager.")
            break

        else:
            print("Invalid choice. Try again.")