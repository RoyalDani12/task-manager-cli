# Task Manager CLI 📝

A simple command-line task manager built with Python that lets you add, list, complete, and remove tasks — all from your terminal.

---

## Features

- Add new tasks with a title, priority, and due date
- List all tasks
- View only pending tasks
- Mark tasks as done
- Remove tasks
- View completed tasks

---

## Project Structure

```
task_manager/
├── main.py        # Entry point — runs the menu loop
├── action.py      # All task functions (add, list, remove, etc.)
├── database.py    # In-memory task storage (list)
└── README.md
```

---

## How to Run

Make sure you have Python installed (3.6 or higher), then run:

```bash
python main.py
```

No external libraries needed — this project uses only built-in Python.

---

## Usage

When you run the program you will see this menu:

![Task Manager CLI Menu](https://github.com/user-attachments/assets/0afa58a1-1c06-4803-8fde-e6ea8c026f3d)

Type the number of the option you want and press Enter.

### Adding a task

```
Task title: Buy groceries
Priority (low/medium/high): high
Due date (YYYY-MM-DD or blank): 2024-12-01
```

### Listing tasks

```
--- All Tasks ---
  1. [⏳ pending] Buy groceries | Priority: high | Due: 2024-12-01
  2. [✅ done   ] Read Python docs | Priority: medium | Due: No due date
```

---

## What I Learned Building This

- Structuring a Python project across multiple files
- Using `import` to share data between modules
- Working with lists and dictionaries
- Input validation with `isdigit()` and `strip()`
- Using `enumerate()` to display numbered lists
- The `pop(index)` method for removing items from a list
- Separation of concerns — keeping data, logic, and UI in separate files

---

## Planned Improvements

- [ ] Save tasks to a file so they persist after closing the program
- [ ] Add task editing
- [ ] Add due date sorting
- [ ] Add color output using the `colorama` library

---

## Author

Built by a Python developer in training 🐍  
Learning one function at a time.
