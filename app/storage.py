from app.models import Task


class TaskStorage:
    """In-memory storage for tasks."""

    def __init__(self):
        self._tasks = []
        self._next_id = 1

    def add(self, title: str) -> Task:
        task = Task(self._next_id, title)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_all(self) -> list[Task]:
        return list(self._tasks)

    def find(self, task_id: int) -> Task | None:
        for task in self._tasks:
            if task.task_id == task_id:
                return task
        return None
