from app.storage import TaskStorage
from app.validators import validate_title


class TaskService:
    """Business logic for task management."""

    def __init__(self, storage=None):
        self.storage = storage or TaskStorage()

    def create_task(self, title: str):
        clean_title = validate_title(title)
        return self.storage.add(clean_title)

    def list_tasks(self):
        return self.storage.get_all()

    def complete_task(self, task_id: int) -> bool:
        task = self.storage.find(task_id)
        if task is None:
            return False

        task.completed = True
        return True
