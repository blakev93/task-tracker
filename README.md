# Task Tracker CLI

A simple command-line application to manage your tasks. Add, update, delete, and track tasks by status — all stored locally in a JSON file.

Built as part of the [roadmap.sh Task Tracker project](https://roadmap.sh/projects/task-tracker).

---

## Requirements

- Python 3.10+
- No external dependencies

---

## Setup

Clone the repo and navigate to the project directory:

```bash
git clone https://github.com/yourusername/task-tracker.git
cd task-tracker
```

No installation required. Run directly with Python:

```bash
python main.py
```

A `tasks.json` file will be created automatically on first run.

---

## Usage

### Add a task
```bash
python main.py add "Buy groceries"
```

### Update a task's description
```bash
python main.py update 1 "Buy groceries and cook dinner"
```

### Delete a task
```bash
python main.py delete 1
```

### Mark a task as in progress
```bash
python main.py mark-in-progress 1
```

### Mark a task as done
```bash
python main.py mark-done 1
```

### List all tasks
```bash
python main.py list
```

### List tasks by status
```bash
python main.py list todo
python main.py list in-progress
python main.py list done
```

---

## Data

Tasks are stored in `tasks.json` in the project root. Each task has the following fields:

| Field | Description |
|---|---|
| `id` | Auto-incremented integer |
| `description` | Task description |
| `status` | `todo`, `in-progress`, or `done` |
| `createdAt` | Timestamp when the task was created |
| `updatedAt` | Timestamp when the task was last updated |
