# actions.py
from database import tasks

def add_task():
    print("\n--- Add New Task ---")
    title = input("Task title: ").strip()
    if not title:
        print("Error: Title cannot be empty.")
        return
    
    priority = input("Priority (low/medium/high): ").strip().lower()
    if priority not in ["low", "medium", "high"]:
        priority = "medium"
        
    due_date = input("Due date (YYYY-MM-DD or blank): ").strip()
    if not due_date:
        due_date = "No due date"

    task = {
        "title": title,
        "priority": priority,
        "due_date": due_date,
        "done": False
    }
    
    tasks.append(task)
    print(f"Success: Task '{title}' added.")

def list_tasks():
    print("\n--- Current Tasks ---")
    if not tasks:
        print("Your task list is empty.")
        return

    # Using enumerate to give each task a visible ID
    for index, task in enumerate(tasks):
        status = "✅" if task["done"] else "pending"
        print(f"{index + 1}. [{status}] {task['title']} | Priority: {task['priority']} | Due: {task['due_date']}")