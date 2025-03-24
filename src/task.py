from datetime import datetime

class Task:

    valid_priorities = ['Low', 'Medium', 'High']


    def __init__(self, title, description, due_date, status, priority='Medium', is_completed=False):  # Fixed parameter order
        self.validate_title(title)
        self.validate_date(due_date)
        self.validate_status(status)   
        self.validate_priority(priority)
        
        self.priority = priority
        self.title = title.strip()
        self.description = description
        self.due_date = due_date
        self.status = status
        self.is_completed = is_completed

    @staticmethod
    def validate_title(title):
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")
        if len(title.strip()) < 3:
            raise ValueError("Title must be at least 3 characters long")

    @staticmethod
    def validate_date(date_str):
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")

    @staticmethod
    def validate_status(status):
        valid_statuses = ['Not Started', 'In Progress', 'Completed']
        if status not in valid_statuses:
            raise ValueError(f"Status must be one of: {', '.join(valid_statuses)}")

    @staticmethod
    def validate_priority(priority):
        if priority not in Task.valid_priorities:
            raise ValueError(f"Priority must be one of: {', '.join(Task.valid_priorities)}")


    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status,
            "is_completed": self.is_completed,
            "priority": self.priority
        }
    
    

