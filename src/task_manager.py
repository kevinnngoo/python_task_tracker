import json
from .task import Task


#class handling all task-related logic
class TaskManager:
    VALID_STATUSES = ['Not Started', 'In Progress', 'Completed']
    
    def __init__(self):
        self.tasks = self.load_tasks()

    #this function tries to read the JSON file, checks if the data is a list
    # then returns the list of tasks, or returns an empty list 
    # if the file is not found or corrupted
    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
                # Validate loaded data
                if not isinstance(tasks, list):
                    raise ValueError("Invalid tasks data format")
                return tasks
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Warning: Tasks file is corrupted. Starting with empty task list.")
            return []
        except Exception as e:
            print(f"Error loading tasks: {str(e)}")
            return []

    #this function writes the list of tasks to the JSON file
    def save_tasks(self):
        try:
            with open("tasks.json", "w") as file:
                #below writes the list of tasks to the file and formats it
                json.dump(self.tasks, file, indent=4)
        except Exception as e:
            print(f"Error saving tasks: {str(e)}")
            raise

    #add a task to the list of tasks
    def add_task(self, task_dict):
        if task_dict['status'] not in self.VALID_STATUSES:
            raise ValueError(f"Status must be one of: {', '.join(self.VALID_STATUSES)}")
        self.tasks.append(task_dict)
        self.save_tasks()

    def update_task(self, index, field, value):
        if 0 <= index < len(self.tasks):
            if field == 'status' and value not in self.VALID_STATUSES:
                raise ValueError(f"Status must be one of: {', '.join(self.VALID_STATUSES)}")
            self.tasks[index][field] = value
            self.save_tasks()

    def delete_task(self, index):
        #ensures the index is not negative, and that it's less than the 
        #length of the list
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()

    def get_tasks(self):
        return self.tasks

