import unittest
from unittest.mock import patch, mock_open
import json
from todo import TodoList

class TestTodoListPersistence(unittest.TestCase):

    def test_load_from_file(self):
        """Test loading todos from a file."""
        mock_data = json.dumps([{'task': 'Test Task', 'completed': False}])
        with patch('builtins.open', mock_open(read_data=mock_data)) as mock_file:
            todo_list = TodoList('test.json')
            self.assertEqual(len(todo_list.todos), 1)
            self.assertEqual(todo_list.todos[0]['task'], 'Test Task')
            mock_file.assert_called_with('test.json', 'r')

    def test_load_file_not_found(self):
        """Test handling of FileNotFoundError."""
        with patch('builtins.open', side_effect=FileNotFoundError) as mock_file:
            todo_list = TodoList('non_existent.json')
            self.assertEqual(len(todo_list.todos), 0)
            mock_file.assert_called_with('non_existent.json', 'r')

    def test_load_json_error(self):
        """Test handling of JSONDecodeError."""
        with patch('builtins.open', mock_open(read_data='invalid json')) as mock_file:
            todo_list = TodoList('bad.json')
            self.assertEqual(len(todo_list.todos), 0)
            mock_file.assert_called_with('bad.json', 'r')

    def test_save_to_file(self):
        """Test saving todos to a file."""
        m = mock_open(read_data='[]')
        with patch('builtins.open', m):
            todo_list = TodoList('test.json')
            todo_list.add_todo('Test Task')

            m.assert_any_call('test.json', 'r')
            m.assert_called_with('test.json', 'w')

            handle = m()
            written_content = "".join(call.args[0] for call in handle.write.call_args_list)

            expected_data = [{'task': 'Test Task', 'completed': False}]
            self.assertEqual(json.loads(written_content), expected_data)


    @patch.object(TodoList, 'save_to_file')
    def test_add_todo_autosaves(self, mock_save_to_file):
        """Test that add_todo calls save_to_file."""
        with patch('builtins.open', mock_open(read_data='[]')):
            todo_list = TodoList('test.json')
            todo_list.add_todo('New Task')
            mock_save_to_file.assert_called_once()

if __name__ == '__main__':
    unittest.main()
