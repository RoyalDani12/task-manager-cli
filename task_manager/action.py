# actions.py
from database import tasks,save_data

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
    save_data()
    print(f"Success: Task '{title}' added.")

def list_tasks():
    print("\n--- Current Tasks ---")
    if not tasks:
        print("Your task list is empty.")
        return

    # Using enumerate to give each task a visible ID
    for index, task in enumerate(tasks):
        status = "done" if task["done"] else "pending"
        print(f"{index + 1}. [{status}] {task['title']} | Priority: {task['priority']} | Due: {task['due_date']}")


# show pending tasks 
def show_pending_task():
    
     print("\n--- Pending Tasks ---")
     pending =[]
     for task in tasks:
         if not task["done"]:
             pending.append(task)
     if not pending :
        print("No pending task.")
        return
     for index,task in enumerate(pending,1):
         print(f"{index}. {task["title"]} | priority : { task["priority"]} | Due :{task["due_date"]}")

def mark_as_done():
    list_tasks()
    id = input("Enter the Id of Task you want to mark done ").strip()
    if not id.isdigit():
        print("Invalid input. please enter a number")
        return
    index = int(id) - 1
    
    if index <0 or index >= len(tasks):
        print("No task found with that number")
        return
    tasks[index]["done"] = True
    print(f"task {tasks[index] ["title"]}  mark as done .Congrats")
    save_data()
    
#   WOrk with removing task from  the json
def remove_task():
    list_tasks()
    id = input("Enter the Id of task  you want to remove (Delete). : ").strip()
    if not id.isdigit():
        print("Invalid input,PLease enter the valid input please")
        return
    index = int(id) -1
    
    if index < 0 or index>= len(tasks):
        print("Please enter a valid input")
        return
    tasks.pop(index)
    save_data()
    print(f"task {tasks[index]["title"]} removed (deleted successfully)")
        

    