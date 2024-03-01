class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, priority=0):
        self.tasks.append((task, priority))
        self.tasks.sort(key=lambda x: x[1])

    def remove_task(self, task):
        self.tasks = [t for t in self.tasks if t[0] != task]

    def show_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for index, (task, priority) in enumerate(self.tasks, start=1):
                print(f"{index}. {task} (Priority: {priority})")
        else:
            print("No tasks in the list.")

    def prioritize_task(self, task, priority):
        for idx, (t, _) in enumerate(self.tasks):
            if t == task:
                self.tasks[idx] = (task, priority)
                self.tasks.sort(key=lambda x: x[1])
                return
        print("Task not found in the list.")

# Example usage
todo = ToDoList()
todo.add_task("Buy groceries", priority=2)
todo.add_task("Finish report", priority=1)
todo.add_task("Call mom")
todo.show_tasks()

todo.remove_task("Call mom")
todo.show_tasks()

todo.prioritize_task("Finish report", 3)
todo.show_tasks()
