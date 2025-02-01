import unittest
from unittest.mock import patch, MagicMock, mock_open
from scripts.main import TaskTracker
from datetime import datetime

class TestTaskTracker(unittest.TestCase):

    @patch('scripts.utils.Utils.create_json_file')
    @patch('os.path.join')
    @patch('os.mkdir')
    @patch('os.getcwd')
    @patch("os.path.exists")
    def test_initializaiton(self, mock_exists, mock_getcwd, mock_mkdir, mock_join, mock_create_file):
        
        data_path = 'backend/task_tracker'

        mock_getcwd.return_value = data_path
        
        mock_join.side_effect = lambda *args: '/'.join(args)


        # Test if folder exists
        mock_exists.return_value = True
        tasks = TaskTracker()
        self.assertEqual(tasks.file_path, 'backend/task_tracker/data/tasks.json')
        mock_mkdir.assert_not_called()       

        mock_mkdir.reset_mock() 
        mock_create_file.reset_mock()
        
        # Test if folder doesn't exist
        mock_exists.return_value = False
        tasks = TaskTracker()
        self.assertEqual(tasks.file_path, 'backend/task_tracker/data/tasks.json')
        mock_mkdir.assert_called_once()
        mock_create_file.assert_called_once_with('backend/task_tracker/data/tasks.json')



    @patch('builtins.open', new_callable=mock_open, read_data='{"Tasks": []}')
    @patch('scripts.utils.Utils.generate_id', return_value=1)
    @patch('datetime.datetime')
    def test_addTasks(self, mock_datetime, mock_generate_id, mock_open ):

        mock_datetime.now.return_value = datetime(2025, 1, 1, 10, 0, 0,0)

        mock_task = {
            "id" : 1, 
            "description" : "mock description",
            "status" : "not done",
            "createdAt" : "2025-01-01 10:00:00.0",
            "updatedAt" : "2025-01-01 10:00:00.0"
        }

        mock_file_path = 'mock.json'

        tasks = TaskTracker()
        tasks.file_path = mock_file_path
        returned_id = tasks.addTask("mock description")

        self.assertEqual(returned_id, 1)

        mock_open.assert_called_once_with(mock_file_path, 'r+')


        opening_data = mock_open()
        opening_data.seek.assert_called_once_with(0)
        

if __name__ == '__main__':
    unittest.main()        