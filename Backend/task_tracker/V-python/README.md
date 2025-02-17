# Task Tracker Application

This project includes a Task Tracker application that allows users to manage tasks through a command-line interface.

## Getting Started

These instructions will help you set up and run the Task Tracker application on your local machine.

### Prerequisites

Make sure you have Python installed on your system.

### Installation

1. Clone the repository to your local machine:
```bash
git clone <repository-url>
```

2. Navigate to the project directory:
```
cd Backend/V-python/task_tracker
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```


## Usage

### Running the Task Tracker CLI

1. Start the Task Tracker CLI by running the following command:
```bash
python3 tasks_shell.py
```
2. Use the following commands in the CLI to interact with the Task Tracker:
- `add <description>`: Add a new task with the specified description.
- `list [statusType]`: List all tasks or tasks with a specific status type.
- `update <id> <description>`: Update the description of a task with the specified ID.
- `delete <id>`: Delete the task with the specified ID.
- `mark <status> <id>`: Update the status of a task with the specified ID.

### Running Unit Tests

1. Run the unit tests using the following command:
```bash
python3 tests/main_test.py
```
