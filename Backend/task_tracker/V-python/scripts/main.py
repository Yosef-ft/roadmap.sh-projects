import os
import json
from .utils import Utils
from datetime import datetime
from typing import *


class TaskTracker:
    def __init__(self):
        self.file_path = 'task_tracker/data'

        self.file_path = os.path.join(os.path.split(os.getcwd())[0], self.file_path)
        if not os.path.exists(self.file_path):
            os.mkdir(self.file_path)

        self.file_path = os.path.join(self.file_path, 'tasks.json')
        Utils.create_json_file(self.file_path)


    def addTask(self, description: str):
        
        with open(self.file_path, 'r+') as file:
            tasks = json.load(file)
            task_dict = {
                "id" : Utils.generate_id(self.file_path),
                "description" : description,
                "status" : "not done",
                "createdAt" : str(datetime.now()),
                "updatedAt" : str(datetime.now())
            }
            tasks['Tasks'].append(task_dict)
            file.seek(0)
            json.dump(tasks, file, indent=4)

            return task_dict['id']
        
    
    def updateTask(self, id: int, updatedTask: str):

        with open(self.file_path, 'r') as file:
            tasks = json.load(file)

            for task in tasks['Tasks']:
                if task['id'] == id:
                    task.update({"description": updatedTask})
            
        with open(self.file_path, 'w') as file:
            json.dump(tasks, file, indent=4)



    def deleteTask(self, id: int):

        with open(self.file_path, 'r') as file:
            tasks = json.load(file)

            for inx, task in enumerate(tasks['Tasks']):
                if task['id'] == id:
                    tasks['Tasks'].pop(inx)

        with open(self.file_path, 'w') as file:
            json.dump(tasks, file, indent=4)


    def updateStatus(self, statusType:str, id: int):

        with open(self.file_path, 'r') as file:
            tasks = json.load(file)

            for task in tasks['Tasks']:
                if task['id'] == id:
                    task.update({"status": statusType})        

        with open(self.file_path, 'w') as file:
            json.dump(tasks, file, indent=4)     

    def listTasks(self, statusType: Optional[str] = None):
        with open(self.file_path, 'r') as file:
            tasks = json.load(file) 

        if statusType == None:
            for task in tasks['Tasks']:
                print(task)
        else:
            for task in tasks['Tasks']:
                if task['status'] == statusType:
                    print(task)


if __name__ == "__main__":
    task = TaskTracker()
    task.addTask('Learn backend')