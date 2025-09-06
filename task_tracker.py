import json
import os

# File where all tasks will be stored
TASKS_FILE = "tasks.json"


# ------------------------------
# Load existing tasks from file
# ------------------------------
def load_tasks():
    # Check if the file exists, otherwise return an empty list
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            # Convert JSON file -> Python list of tasks
            return json.load(f)
    return []  # No file yet, so return an empty task list


# ------------------------------
# Save tasks back into file
# ------------------------------
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        # Convert Python list -> JSON and write to file
        json.dump(tasks, f, indent=4)  # indent=4 makes it human-readable


# ------------------------------
# Add a new task
# ------------------------------
def add_task(tasks, description):
    # A task is represented as a dictionary (Python’s version of a JSON object)
    task = {"description": description, "done": False}

    # Add it to the existing list of tasks
    tasks.append(task)

    # Save the updated list to the file
    save_tasks(tasks)

    # Feedback to the user
    print(f"✅ Task added: {description}")


# ------------------------------
# Main loop (entry point)
# ------------------------------
def main():
    # Load tasks from file (or empty if first run)
    tasks = load_tasks()
    print("\nWhat do you want to do?")
    print("1. Add task")
    print("2. List tasks")

    # Ask user to type a new task
    desc = input("Enter a task: ")

    # Add the task to the list + save
    add_task(tasks, desc)


# ------------------------------
# Python convention:
# Only run main() if script is run directly
# (not when imported as a module)
# ------------------------------
if __name__ == "__main__":
    main()
