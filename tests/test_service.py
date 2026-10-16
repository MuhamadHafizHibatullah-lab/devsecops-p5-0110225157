
import unittest

from app.service import TaskService


class TestTaskService(unittest.TestCase):

    def setUp(self):
        self.service = TaskService()

    def test_create_task(self):
        task = self.service.create_task("Belajar DevSecOps")
        self.assertEqual(task.title, "Belajar DevSecOps")
        self.assertEqual(task.task_id, 1)

    def test_reject_empty_title(self):
        with self.assertRaises(ValueError):
            self.service.create_task(" ")

    def test_complete_task(self):
        task = self.service.create_task("Mengerjakan tugas")
        self.assertTrue(self.service.complete_task(task.task_id))
        self.assertTrue(task.completed)

    def test_unknown_task(self):
        self.assertFalse(self.service.complete_task(999))


if __name__ == "__main__":
    unittest.main()
