
# Task Manager CLI

A simple command-line task manager that stores tasks in a local JSON file. It allows you to add, update, delete, list tasks, and change their status.

## Data Storage

All tasks are stored in a file called `database.json`. If the file doesn't exist or is invalid, it will be created automatically.

## Usage

Run the script with Python 3:

```bash
python task-cli.py <command> [arguments...]
```
---

## Commands

### `add <description>`
Adds a new task with the given description.

```bash
python task-cli.py add "Buy groceries"
```

---

### `update <id> <new_description>`
Updates the description of an existing task by its ID.

```bash
python task-cli.py update 1 "Buy groceries and fruits"
```

---

### `delete <id>`
Deletes a task by its ID.

```bash
python task-cli.py delete 2
```

---

### `list <status>`
Displays all tasks. Optionally filter by status: `todo`, `in-progress`, or `done`.

```bash
python task-cli.py list
```

```bash
python task-cli.py list done
```

---

### `mark-todo <id>`  
### `mark-in-progress <id>`  
### `mark-done <id>`
Updates the status of a task.

```bash
python task-cli.py mark-done 3
```

---

## Task Structure

Each task is stored in the following format:

```json
{
  "id": 1,
  "description": "Buy groceries",
  "status": "todo",
  "createdAt": "07/12/25 13:45",
  "updatedAt": "07/12/25 13:45"
}
```

---

## Notes

- Invalid commands or missing arguments are silently ignored.
- Timestamps are recorded on creation and update.
- All interaction is handled via `sys.argv`.
