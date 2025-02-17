import * as fs from 'fs';
import * as path from 'path';
import { json } from 'stream/consumers';

type Status = 'todo' | 'in-progress' | 'done' 

interface Task{
  id: number,
  description: string,
  status: Status,
  createdAt: string,
  updatedAt: string
}


export class TaskTracker {
  private filepath: string

  constructor(){
    this.filepath = path.join(process.cwd(), 'data/tasks.json')
    this.ensureFileExists();
  }

  private ensureFileExists() {
    const dir = path.dirname(this.filepath)

    if (!fs.existsSync(dir)){
      fs.mkdirSync(dir)
    }

    if (!fs.existsSync(this.filepath)){
      fs.writeFileSync(this.filepath, JSON.stringify({ Tasks : []}, null, 4))
    }
  }

  private readTask() : {Tasks : Task[]}{
    return JSON.parse(fs.readFileSync(this.filepath, 'utf-8'))
  }


  private writeTask(tasks: Task[]){
    fs.writeFileSync(this.filepath, JSON.stringify({Tasks : tasks}, null, 4))
  }

  addTask(description: string): number {
    const data = this.readTask()
    const newTask: Task = {
      id: data.Tasks.length + 1,
      description: description,
      status: 'todo',
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString()
    }

    data.Tasks.push(newTask)
    this.writeTask(data.Tasks)
    return newTask.id
  }


  updateTask(newDescription: string, id: number): void{
    const data =  this.readTask();
    let task: Task | undefined = data.Tasks.find(task => task.id === id);
    if (task) {
      task.description = newDescription;
      task.updatedAt = new Date().toISOString();
      this.writeTask(data.Tasks);
    } else {
      console.error(`Task with ID ${id} not found.`);
    }
  }
  
}


const tk: TaskTracker = new TaskTracker()
tk.addTask('the first ts task')