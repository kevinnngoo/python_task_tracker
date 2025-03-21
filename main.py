# Python Task Tracker
import json

# The application should run from the command line, accept user actions and inputs as arguments,
# and store the tasks in a JSON file. The user should be able to:
# Add, Update, and Delete tasks
# Mark a task as in progress or done
# List all tasks
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress

# Load existing tasks from JSON file at start
tasks = []

def add_task():
    title = input("Enter the title of your task: ")
    description = input("Enter the description of your task: ")
    due_date = input("Enter the due date of your task: (YYYY-MM-DD)")
    status = input("Enter the status of your task: ")
    is_completed = False

    return {
        "title": title,
        "description": description,
        "due_date": due_date,
        "status": status,
        "is_completed": is_completed
    }

#write a function called load_tasks() to read the tasks from the JSON file to 
#fill your tasks list.

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

#write a function called save_tasks() to save the tasks to a JSON file.

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# write a function called update_tasks() to update the tasks in the JSON file.
def update_tasks():
    choose_task = int(input("Enter the number of the task you want to update: "))
    index = choose_task - 1  # Adjust for 0-based indexing

    # ask which part they would like to update (title, description, due_date, status)
    update_part = input("Enter the part you want to update (title, description, due_date, status): ")

    if update_part == "title":
        tasks[index]["title"] = input("Enter the new title: ")
    elif update_part == "description":
        tasks[index]["description"] = input("Enter the new description: ")
    elif update_part == "due_date":
        tasks[index]["due_date"] = input("Enter the new due date (YYYY-MM-DD): ")
    elif update_part == "status":
        tasks[index]["status"] = input("Enter the new status: ")

    save_tasks()


# write a function called delete_tasks() to delete the tasks in the JSON file.
def delete_tasks():
    # show the list of tasks
    view_tasks()

    choose_task = int(input("Enter the number of the task you want to delete: "))
    index = choose_task - 1  # Adjust for 0-based indexing

    tasks.pop(index)
    save_tasks()


# Make sure to call load_tasks at the beginning to fill the tasks list
tasks = load_tasks()

#write a function named view_tasks() to display the tasks in a readable format.
def view_tasks():
    print("Tasks:")
    for task in tasks:
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Due Date: {task['due_date']}")
        print(f"Status: {task['status']}")
        print(f"Completed: {task['is_completed']}")
        print()

#While loop to prompt these things:
# Add tasks
# View tasks
# Update or delete tasks
# Quit the program

while True:
    print("Choose an option:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update or Delete Task")
    print("4. Quit")

    choice = int(input("Type the number of your choice: "))

    if choice == 1:
        task = add_task()
        tasks.append(task)
        save_tasks()
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        print("Choose an action:")
        print("1. Update Task")
        print("2. Delete Task")
        sub_choice = int(input("Enter your choice (1 or 2): "))
        if sub_choice == 1:
            update_tasks()
        elif sub_choice == 2:
            delete_tasks()
        else:
            print("Invalid choice. Please try again.")
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")
