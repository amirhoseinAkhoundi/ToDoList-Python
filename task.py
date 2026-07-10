class Task:
    #structure of the tasks
    def __init__(self , task_id, title, description, priority, completed=False) :
            self.task_id = task_id
            self.title = title
            self.description = description
            self.priority = priority
            self.completed = completed
            
            
    def __str__(self):
        #how task will be shown
        status = "✅ Completed" if self.completed else "❌ Pending"
        return f"{self.task_id} | {self.title} | {self.description} | {self.priority} | {status} "
    
    