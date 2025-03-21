#Python Task Tracker
import json
# The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:

# Add, Update, and Delete tasks
# Mark a task as in progress or done
# List all tasks
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress

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
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
        return tasks
    
#write a function called save_tasks to save the tasks to the JSON file.

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
