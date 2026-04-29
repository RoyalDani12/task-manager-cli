


#   lets  prepare the menu
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
  print("\n"+"="*40)
  print(" "*10+"Task Manager CLI")
  print("="*40)
  for key,label in MENU.items():
    print(f"[{key}] {label}")
  print("="*40)
# print_menu()

#  main with  the while loop
def main():
  print("Welcome to task manager")
  
  while True:
    print_menu()
    
    choice = input("choose : ").strip().lower()
    
    if choice =="q":
      print("Goodbye!")
      break
    if choice == "1":
        add_task()
    else:
        print("menu choice coming soon")
    
    if choice not in MENU:
      print("Invalid option. Try again.")
      continue
    
    print(f" you picked : {MENU[choice]}")


     
tasks =[]

def add_task():
  print("\n----Add new task -----")
  title = input("Task title :").strip()
  if not title :
    print("Title can not be empty")
    return
  
  priority = input(" priority (low/medium/high) : ").strip().lower()
  if priority not in ["low","medium","high"]:
      priority ="medium"
      
  due_date = input("Due date (YYY-MM-DD or leave blank) : ")
  if not due_date:
    due_date ="No due date"
  #  build  tasks as a dict
  
  task ={
    "title":title,
    "priority":priority,
    "due_date":due_date,
    "done":False
  }
  
  #  add task to the list
  tasks.append(task)
  print(f"task {title} add successfully")
  
  
if __name__=="__main__":
     main()