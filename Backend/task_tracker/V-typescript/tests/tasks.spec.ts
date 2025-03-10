import { beforeEach, describe, it, expect, vi, afterEach } from "vitest";
import * as fs from 'fs'
import * as path from 'path'
import {TaskTracker} from '../src/main'
import exp from "constants";
import { json } from "stream/consumers";

describe("Task tests", () =>{
  let tracker: TaskTracker;


  beforeEach(() =>{
    vi.mock('fs', async(importOriginal) => {

      const actual = (await importOriginal()) as typeof fs;

      return {
        ...actual,
        existsSync: vi.fn((filepath: string) => filepath === path.join(process.cwd(), 'data/tasks.json')),
        mkdirSync: vi.fn(() => undefined),
        readFileSync: vi.fn((filepath) => JSON.stringify({Tasks : []})),
        writeFileSync: vi.fn(()=> {})

      };
    });

    
  });


  afterEach(() =>{
    vi.resetAllMocks()
  });


  it('should create new task and return ID', ()=>{
    
    tracker = new TaskTracker()
    const taskID = tracker.addTask('Test task')

    expect(taskID).toBe(1)
    expect(fs.writeFileSync).toHaveBeenCalledTimes(2)
  })


  it('should create the data directory if it doesn\'t exist', () =>{
    vi.spyOn(fs, 'existsSync').mockReturnValue(false);
    tracker['ensureFileExists']();

    expect(fs.mkdirSync).toHaveBeenCalledOnce()
  })

  
  it('should update the task', () => {
   
    const mockTasks = { Tasks: [{ id: 1, description: 'first Task', updatedAt: '' }] };

    vi.spyOn(fs, 'readFileSync').mockReturnValue(JSON.stringify(mockTasks));

    const writeSpy = vi.spyOn(fs, 'writeFileSync');

    tracker.updateTask('Updated Task', 1);

    const writtenData = JSON.parse(writeSpy.mock.calls[0][1] as string); 

    expect(writtenData.Tasks[0].description).toBe('Updated Task');
    expect(writeSpy).toHaveBeenCalledTimes(1); 
  });


  it('should delete a task', () =>{
    const mockTasks = { Tasks: [{ id: 1, description: 'first Task', updatedAt: '' }] };

    vi.spyOn(fs, 'readFileSync').mockReturnValue(JSON.stringify(mockTasks))

    const writeSpy = vi.spyOn(fs, 'writeFileSync');

    tracker.deleteTask(1);

    const writtenData = JSON.parse(writeSpy.mock.calls[0][1] as string)

    expect(writtenData.Tasks.length).toBe(0)
  })


  it('should update the status', () =>{
    const mockTasks = { Tasks: [{ id: 1, description: 'first Task', status: 'todo' }] };

    vi.spyOn(fs, 'readFileSync').mockReturnValue(JSON.stringify(mockTasks))

    const writeSpy = vi.spyOn(fs, 'writeFileSync')

    tracker.updateStatus(1, 'done')
    
    const updatedTask = JSON.parse(writeSpy.mock.calls[0][1] as string)
    expect(updatedTask.Tasks[0].status).toBe('done')
  })

})