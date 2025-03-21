class Task:
    def __init__(self, title, description, due_date, status, is_completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
        self.is_completed = is_completed

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status,
            "is_completed": self.is_completed
        }