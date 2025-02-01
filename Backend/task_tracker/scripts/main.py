import os
import json

class TaskTracker:
    def __init__(self):
        self.file_path = 'task_tracker/data'

        self.file_path = os.path.join(os.path.split(os.getcwd())[0], self.file_path)
        if not os.path.exists(self.file_path):
            os.mkdir(self.file_path)



if __name__ == "__main__":
    task = TaskTracker()
