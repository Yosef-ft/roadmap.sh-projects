import { beforeEach, describe, it, expect, vi, afterEach } from "vitest";
import * as fs from 'fs'
import * as path from 'path'
import {TaskTracker} from '../src/main'
import { JsxEmit } from "typescript";

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

})