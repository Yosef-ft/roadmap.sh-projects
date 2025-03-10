import cmd
from scripts.main import TaskTracker


class TaskShell(cmd.Cmd):
    intro = "Welcome to task tracker"
    prompt = 'task-cli'

    def __init__(self, completekey = "tab", stdin = None, stdout = None):
        super().__init__(completekey, stdin, stdout)
        self.tracker = TaskTracker()

    def do_add(self, arg):
        description: str = arg.replace("\"", '').strip()
        if description != '':
            id = self.tracker.addTask(description)
            print(f"Task added successfully (ID: {id})")

    def do_list(self, arg):
        if arg != '':
            print(arg)
            self.tracker.listTasks(arg)
        else:
            self.tracker.listTasks()

    def do_update(self, arg):
        args = arg.split(' ')
        id: int = args[0]
        args.pop(0)
        description: str = ' '.join(args).replace("\"", '').strip()
        self.tracker.updateTask(int(id), description)


    def do_delete(self, arg):
        id: int = int(arg)
        self.tracker.deleteTask(id)

    def do_mark(self, arg):
        args = arg.split(' ')
        id: int = int(args[1])
        status: str = args[0].replace('-', ' ').strip()
        self.tracker.updateStatus(status, id)


    def do_exit(self, arg):
        print("Exiting task-cli")
        return True

if __name__ == "__main__":
    TaskShell().cmdloop()