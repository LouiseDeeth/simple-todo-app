import unittest
from todo import TodoList
import os

class TestTodoList(unittest.TestCase):

    def setUp(self):
        """Set up a new TodoList for each test."""
        self.filename = "test_todos.json"
        # Ensure the file does not exist before each test
        if os.path.exists(self.filename):
            os.remove(self.filename)
        self.todo_list = TodoList(filename=self.filename)

    def tearDown(self):
        """Clean up the test file after each test."""
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_add_todo(self):
        """Test adding a todo."""
        self.todo_list.add_todo("Test Task 1")
        self.assertEqual(len(self.todo_list.todos), 1)
        self.assertEqual(self.todo_list.todos[0]['task'], "Test Task 1")
        self.assertFalse(self.todo_list.todos[0]['completed'])

    def test_list_todos(self):
        """Test listing todos."""
        self.assertEqual(self.todo_list.list_todos(), [])
        self.todo_list.add_todo("Test Task 1")
        self.todo_list.add_todo("Test Task 2")
        todos = self.todo_list.list_todos()
        self.assertEqual(len(todos), 2)
        self.assertEqual(todos[0]['task'], "Test Task 1")
        self.assertEqual(todos[1]['task'], "Test Task 2")

if __name__ == '__main__':
    unittest.main()
