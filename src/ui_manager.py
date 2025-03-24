from datetime import datetime
from .task_manager import TaskManager


"""
The UIManager class handles all user interface interactions for the task tracking application.
It provides a command-line interface for users to add, view, update, and delete tasks through
an interactive menu system. The class implements input validation for task attributes like
titles and due dates, and manages the display of task information in a readable format.
It acts as a bridge between the user and the TaskManager class, which handles the underlying
data operations and persistence. Error handling is implemented throughout to ensure a smooth
user experience and prevent data corruption.
"""

class UIManager:
    def __init__(self):
        self.task_manager = TaskManager()

    def get_valid_input(self, prompt, validator_func, error_message):
        while True:
            try:
                user_input = input(prompt).strip()
                validator_func(user_input)
                return user_input
            except ValueError as e:
                print(f"Error: {error_message}")

    def get_status_choice(self):
        print("\nAvailable statuses:")
        for i, status in enumerate(TaskManager.VALID_STATUSES, 1):
            print(f"{i}. {status}")
        
        while True:
            try:
                choice = int(input("Choose status (enter number): "))
                if 1 <= choice <= len(TaskManager.VALID_STATUSES):
                    return TaskManager.VALID_STATUSES[choice - 1]
                print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

    def add_task(self):
        try:
            title = self.get_valid_input(
                "Enter the title of your task: ",
                lambda x: len(x.strip()) >= 3,
                "Title must be at least 3 characters long"
            )

            description = input("Enter the description of your task: ")
            
            due_date = self.get_valid_input(
                "Enter the due date of your task (YYYY-MM-DD): ",
                lambda x: datetime.strptime(x, '%Y-%m-%d'),
                "Invalid date format. Use YYYY-MM-DD"
            )

            status = self.get_status_choice()

            task_dict = {
                "title": title,
                "description": description,
                "due_date": due_date,
                "status": status,
                "is_completed": False
            }
            
            self.task_manager.add_task(task_dict)
            print("\nTask added successfully!")
            
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("Task was not added. Please try again.")



    def view_tasks(self, status_filter=None):
        """
        Displays tasks with optional sorting and filtering.
        
        Parameters:
            status_filter: Optional filter to show only tasks with specific status
        
        Options:
            1. Default order (as stored)
            2. Sorted by due date (ascending)
            3. Sorted by due date (descending)
        """
        print("\nChoose how to view tasks:")
        print("1. Default order")
        print("2. By due date (earliest first)")
        print("3. By due date (latest first)")
        view_choice = int(input("Enter your choice (1, 2, or 3): "))

        if view_choice == 2:
            tasks = self.task_manager.get_tasks_by_due_dates('asc')
        elif view_choice == 3:
            tasks = self.task_manager.get_tasks_by_due_dates('desc')
        else:
            tasks = self.task_manager.get_tasks()

        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            if status_filter and task["status"] != status_filter:
                continue
            print(f"\nTask {i}:")
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Due Date: {task['due_date']}")
            print(f"Status: {task['status']}")
            print(f"Completed: {task['is_completed']}")

    def update_tasks(self):
        self.view_tasks()
        choose_task = int(input("Enter the number of the task you want to update: "))
        index = choose_task - 1

        update_part = input("Enter the part you want to update (title, description, due_date, status): ")
        new_value = input(f"Enter the new {update_part}: ")
        
        self.task_manager.update_task(index, update_part, new_value)

    def delete_tasks(self):
        try:
            self.view_tasks()
            choose_task = self.get_valid_input(
                "Enter the number of the task you want to delete: ",
                lambda x: 1 <= int(x) <= len(self.task_manager.get_tasks()),
                "Invalid task number"
            )
            index = int(choose_task) - 1
            self.task_manager.delete_task(index)
            print("\nTask deleted successfully!")
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("Task was not deleted. Please try again.")

    def run(self):
        while True:
            print("\nChoose an option:")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Update or Delete Task")
            print("4. Quit")

            try:
                choice = int(input("\nType the number of your choice: "))
                
                if choice == 1:
                    self.add_task()
                elif choice == 2:
                    self.view_tasks()
                elif choice == 3:
                    print("\nChoose an action:")
                    print("1. Update Task")
                    print("2. Delete Task")
                    sub_choice = int(input("Enter your choice (1 or 2): "))
                    if sub_choice == 1:
                        self.update_tasks()
                    elif sub_choice == 2:
                        self.delete_tasks()
                    else:
                        print("Invalid choice. Please try again.")
                elif choice == 4:
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
            except IndexError:
                print("Invalid task number. Please try again.")





