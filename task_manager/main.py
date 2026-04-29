# main.py
from action import add_task, list_tasks,show_pending_task,mark_as_done,remove_task

MENU = {
    "1": "Add task",
    "2": "List all tasks",
    "3": "Pending tasks",
    "4": "Mark task as done",
    "5": "Remove task",
    "7": "Completed tasks",
    "q": "Quit",
}

def print_menu():
    print("\n" + "="*40)
    print(" " * 10 + "Task Manager CLI")
    print("="*40)
    for key, label in MENU.items():
        print(f"[{key}] {label}")
    print("="*40)

def main():
    print("Welcome to Task Manager")
    
    while True:
        print_menu()
        choice = input("Choose: ").strip().lower()
        
        if choice == "q":
            print("Goodbye!")
            break
        
        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice =="3":
            show_pending_task()
        elif choice == "4":
            mark_as_done()
        elif choice == "5":
            remove_task()
        elif choice in MENU:
            print(f"Feature '{MENU[choice]}' coming soon.")
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()