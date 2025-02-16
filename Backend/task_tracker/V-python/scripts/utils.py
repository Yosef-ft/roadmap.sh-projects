
import json
import os

class Utils:
   
    @staticmethod
    def create_json_file(file_path):
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                initial = {"Tasks" : []}
                json.dump(initial, file, indent=4)


    @staticmethod
    def generate_id(file_path) -> int:

        with open(file_path, 'r') as file:
            tasks = json.load(file)['Tasks']
            id = len(tasks)

        return id + 1
