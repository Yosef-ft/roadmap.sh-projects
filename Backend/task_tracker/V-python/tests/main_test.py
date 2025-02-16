import os
import sys
import unittest
from unittest.mock import patch, MagicMock, mock_open
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.main import TaskTracker
from datetime import datetime
import json

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


    @patch('builtins.open', new_callable=mock_open, read_data='{"Tasks": [{"id": 1, "description": "mock description", "status": "not done", "createdAt": "2025-01-01 10:00:00.0", "updatedAt": "2025-01-01 10:00:00.0"}]}')
    def test_updateTask(self, mock_file: MagicMock):
        
        mock_file_path = 'mock.json'
        tasks = TaskTracker()
        tasks.file_path = mock_file_path  

        
        tasks.updateTask(1, 'update mock')  

        
        mock_file.assert_any_call(mock_file_path, 'r')  
        mock_file.assert_any_call(mock_file_path, 'w')  

        expected_updated_task = {
            "id": 1,
            "description": "update mock",
            "status": "not done",
            "createdAt": "2025-01-01 10:00:00.0",
            "updatedAt": "2025-01-01 10:00:00.0"
        }    

        expected_written_content = json.dumps({"Tasks": [expected_updated_task]}, indent=4)

       
        handle: MagicMock = mock_file()
        actual_written_content = "".join(call[0][0] for call in handle.write.call_args_list)
        
        self.assertEqual(actual_written_content, expected_written_content)
        

    @patch('builtins.open', new_callable=mock_open, read_data= '{"Tasks": [{"id": 1, "description": "mock description", "status": "not done", "createdAt": "2025-01-01 10:00:00.0", "updatedAt": "2025-01-01 10:00:00.0"}]}')
    def test_delete(self, mock_file: MagicMock):

        mock_file_path = 'mock.json'
        tasks = TaskTracker()
        tasks.file_path = mock_file_path

        tasks.deleteTask(1)

        mock_file.assert_any_call(mock_file_path, 'r')  
        mock_file.assert_any_call(mock_file_path, 'w')

        expected_written_content = json.dumps({"Tasks": []}, indent=4)

        handle: MagicMock = mock_file()
        actual_written_content = "".join(call[0][0] for call in handle.write.call_args_list)

        self.assertEqual(expected_written_content, actual_written_content)


    @patch('builtins.open', new_callable=mock_open, read_data='{"Tasks": [{"id": 1, "description": "mock description", "status": "not done", "createdAt": "2025-01-01 10:00:00.0", "updatedAt": "2025-01-01 10:00:00.0"}]}')        
    def test_updateStatus(self, mock_file: MagicMock):

        mock_file_path = 'mock.json'
        tasks = TaskTracker()
        tasks.file_path = mock_file_path

        tasks.updateStatus('done', 1)

        mock_file.assert_any_call(mock_file_path, 'r')
        mock_file.assert_any_call(mock_file_path, 'w')

        expected_updated_task = {
            "id": 1,
            "description": "mock description",
            "status": "done",
            "createdAt": "2025-01-01 10:00:00.0",
            "updatedAt": "2025-01-01 10:00:00.0"
        }

        expected_updated_content = json.dumps({"Tasks": [expected_updated_task]}, indent=4)

        handle: MagicMock = mock_file()

        actual_written_content = "".join(call[0][0] for call in handle.write.call_args_list)

        self.assertEqual(actual_written_content, expected_updated_content)



if __name__ == '__main__':
    unittest.main()        