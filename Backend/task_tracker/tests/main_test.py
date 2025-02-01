import unittest
from unittest.mock import patch
from scripts.main import TaskTracker

class TestTaskTracker(unittest.TestCase):

    @patch('os.path.join')
    @patch('os.mkdir')
    @patch('os.getcwd')
    @patch("os.path.exists")
    def test_initializaiton(self, mock_exists, mock_getcwd, mock_mkdir, mock_join):
        
        data_path = 'backend/task_tracker'

        mock_getcwd.return_value = data_path
        
        mock_join.side_effect = lambda *args: '/'.join(args)


        # Test if folder doesn't exit
        mock_exists.return_value = True
        tasks = TaskTracker()
        self.assertEqual(tasks.file_path, 'backend/task_tracker/data')
        mock_mkdir.assert_not_called()        
        
        # Test if folder exists
        mock_exists.return_value = False
        tasks = TaskTracker()
        self.assertEqual(tasks.file_path, 'backend/task_tracker/data')
        mock_mkdir.assert_called_once()


if __name__ == '__main__':
    unittest.main()        