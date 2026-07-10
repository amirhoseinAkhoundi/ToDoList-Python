import csv
from task import Task

class ToDoList:
    def __init__(self):
        self.tasks = []
    
    #imports tasks through csv file in the same directory
    def load_from_csv(self):
        try:
            with open("tasks.csv", "r", newline="") as file:
                reader = csv.reader(file)
                
                next(reader)
                
                for row in reader:
                    task = Task(
                        int(row[0]),
                        row[1],
                        row[2],
                        row[3],
                        row[4] == "True"
                    )
                    
                    self.tasks.append(task)
                    
        except FileNotFoundError:
            pass
    
    #to add task manually
    def add_task(self, task):
        if self.find_task(task.task_id):
            print("Task ID already Exists!")
            return
        self.tasks.append(task)
        self.sort_by_priority()
        print("Task Added Successfully")
        
    #Finds tasks based on their ID
    def find_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
            
        return None
    
    #saves all changes to a csv file in same directory 
    def save_to_csv(self):
        with open("tasks.csv", "w", newline="") as file:
            writer = csv.writer(file)
            
            writer.writerow(["ID", "Title", "Description", "Priority", "completed"])
            
            for task in self.tasks:
                writer.writerow([
                    task.task_id,
                    task.title,
                    task.description,
                    task.priority,
                    task.completed
                 ])
    
    #shows all tasks no matter completed or not 
    def view_tasks(self):
        if not self.tasks:
            print("No tasks found!")
            return
        
        for task in self.tasks:
            print(task)
    
    #removes tasks based on id
    def remove_task(self, task_id):
        task = self.find_task(task_id)
        if task:
            self.tasks.remove(task)
            self.save_to_csv()
            print("Task removed successfully!")
        else:
            print("Task not found!")
            
    #marks a task as completed
    def mark_completed(self, task_id):
        task = self.find_task(task_id)

        if not task:
            print("Task not found!")
            return

        if task.completed:
            print("Task is already completed!")
            return

        task.completed = True
        self.save_to_csv()
        print("Task marked as completed!")
    
    #asks for task ID then changes all entries 
    #(could be more specific by using a menu)
    def edit_task(self, task_id, title, description, priority):
        task = self.find_task(task_id)
    
        if task:
            task.title = title
            task.description = description
            task.priority = priority
            self.sort_by_priority()
            print("Task Updated Successfully!")
        else:
            print("Task Not Found!")

    def show_statistics(self):
        total_tasks = len(self.tasks)
        
        completed_tasks = 0
        
        for task in self.tasks:
            if task.completed:
                completed_tasks += 1
        pending_tasks = total_tasks - completed_tasks
        
        if total_tasks == 0:
            completion_rate = 0
        else:
            completion_rate = (completed_tasks / total_tasks) * 100
            
        print("\n===== Statistics ======")
        print(f"Total tasks: {total_tasks}")
        print(f"Completed tasks: {completed_tasks}")
        print(f"Pending tasks: {pending_tasks}")
        print(f"Completion Rate: {completion_rate:.1f}%")
        
    def sort_by_priority(self):
        priority_order = {
            "High": 1,
            "Medium": 2,
            "Low": 3
        }
        
        self.tasks.sort(key=lambda task: priority_order[task.priority])
        self.save_to_csv()    
    