<?php

require_once 'Utils.php';

class TaskTracker{
    private $filePath;

    function __construct() {
        
        $dirName = dirname(__DIR__) . '/V-PHP/data';
        $this->filePath = $dirName . '/tasks.json';


        if (!file_exists($this->filePath)) {
            mkdir($this->filePath, 0777, true); 
        }

        Utils::create_json_file($this->filePath); 
    }


    public function addTask($description){
        $tasks = json_decode(@file_get_contents($this->filePath), true);
        
        if ($tasks === null) {
            $tasks = ['Tasks' => []];
        }
        
        $id_len = count($tasks['Tasks'] ?? []);
        
        $newTask = [
            "id" => $id_len + 1,
            "description" => $description,
            "status" => "not done",
            "createdAt" => date('Y-m-d H:i:s'),
            "updatedAt" => date('Y-m-d H:i:s')
        ];
        
        $tasks['Tasks'][] = $newTask;
        
        file_put_contents($this->filePath, json_encode($tasks, JSON_PRETTY_PRINT));
        
        return $newTask['id'];
    }

    public function updateTask($id, $description){
        $tasks = json_decode(file_get_contents($this->filePath), true);

        foreach($tasks['Tasks'] as &$task){
            if($task['id'] == $id){
                $task['description'] = $description;
                $task['updatedAt'] = date('Y-m-d H:i:s');
                break;
            }
        }

        file_put_contents($this->filePath,json_encode($tasks, JSON_PRETTY_PRINT));

    }

    public function deleteTask($id){
        $tasks = json_decode(file_get_contents($this->filePath), true);

        foreach($tasks['Tasks'] as $key => $task){
            if ($task['id'] == $id){
                unset($tasks['Tasks'][$key]);
                break;
            }
        }

        file_put_contents($this->filePath, json_encode($tasks, JSON_PRETTY_PRINT));
    }

    public function updateStatus(string $statusType, int $id){
        $tasks = json_decode(file_get_contents($this->filePath), true);

        foreach($tasks['Tasks'] as &$task){
            if($task['id'] == $id){
                $task['status'] = $statusType;
                break;
            }
        }

        file_put_contents($this->filePath, json_encode($tasks, JSON_PRETTY_PRINT));
    }

    public function listTasks($statusType = null){
        $tasks = json_decode(file_get_contents($this->filePath), true);

        foreach($tasks['Tasks'] as $task){
            if(!$statusType){
                print_r($task);
            }else{
                if($statusType == $task['status']){
                    print_r($task);
                }
            }
        }
    }
  
}


$t = new TaskTracker();
$t->listTasks('done');