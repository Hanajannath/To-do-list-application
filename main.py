class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.completed = False   # all new tasks start as incomplete
    def mark_completed(self):
        self.completed = True
class ToDoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, description, priority):
        self.tasks.append(Task(description, priority))
        print("Task added successfully!")
    def view_tasks(self):
        if self.tasks == []:
            print("No tasks available.")
            return
        index = 1
        for task in self.tasks:
            if task.completed:
                status = "Completed"
            else:
                status = "Incomplete"
            print(index, task.description, "| Priority:", task.priority, "| Status:", status)
            index += 1
    def edit_task(self, index, description=None, priority=None):
        if 0 < index <= len(self.tasks):
            if description:
                self.tasks[index - 1].description = description
            if priority:
                self.tasks[index - 1].priority = priority
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    def complete_task(self, index):
        if 0 < index <= len(self.tasks):
            self.tasks[index - 1].mark_completed()
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
def main():
    todo = ToDoList()
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Mark Task Completed")
        print("4. View Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            desc = input("Enter task description: ")
            prio = input("Enter task priority (High/Medium/Low): ")
            todo.add_task(desc, prio)
        elif choice == "2":
            todo.view_tasks()
            try:
                num = int(input("Enter task number to edit: "))
                desc = input("Enter new description (press Enter to skip): ")
                prio = input("Enter new priority (press Enter to skip): ")
                if desc == "":
                    desc = None
                if prio == "":
                    prio = None
                todo.edit_task(num, desc, prio)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "3":
            todo.view_tasks()
            try:
                num = int(input("Enter task number to mark completed: "))
                todo.complete_task(num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            todo.view_tasks()

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")
if __name__ == "__main__":
    main()
