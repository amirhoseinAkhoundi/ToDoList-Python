#It's so f**king simple innit?

from task import Task
from todo import ToDoList

todo = ToDoList()
todo.load_from_csv()

def get_priority():
        while True:
            priority = input("Priority (High/Medium/Low): ").strip().lower()
            
            if priority in ["high", "medium", "low"]:
                priority = priority.capitalize()
                return priority
            
            print("Invalid priority! Please enter High, Medium or Low.")

def menu ():
        print("\n===== TO DO LIST =====")
        print("1. Add Task")
        print("2. See Tasks")
        print("3. Remove Task")
        print("4. Mark Task")
        print("5. Edit Task")
        print("6. Statistics")
        print("7. Sort by Priority")
        print("8. Exit")
        return input("Enter your choice: ")
    
while True:
    choice = menu()
    if choice == "1":
        task_id = int(input("Task ID: "))
        title = input("Title: ")
        description = input("Description: ")
        priority = get_priority()
            
        task = Task(task_id, title, description, priority)
        
        todo.add_task(task)
            
    elif choice == "2":
        todo.view_tasks()
            
    elif choice == "3":
        task_id = int(input("Enter task ID to remove: "))
        todo.remove_task(task_id)
        
    elif choice == "4":
        task_id = int(input("Enter Task ID to mark as completed: "))
        todo.mark_completed(task_id)
            
    elif choice == "5":
        task_id = int(input("Enter Task ID: "))
            
        title = input("New Title: ")
        description = input("New Description: ")
        priority = input("New Priority: ")
            
        todo.edit_task(task_id, title, description, priority)
    
    elif choice == "6":
        todo.show_statistics()
            
    elif choice == "7":
        todo.sort_by_priority()
        print("Tasks sorted successfully")
        
    elif choice == "8":
        print("Goodbye")
        break
        
    else:
        print("Invalid choice!")