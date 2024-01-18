class TodoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task['description']} - {'Done' if task['completed'] else 'Not Done'}")

    def add_task(self, description):
        task = {'description': description, 'completed': False}
        self.tasks.append(task)
        print(f"Task added: {description}")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            print(f"Task deleted: {deleted_task['description']}")
        else:
            print("Invalid task index.")

    def mark_as_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]['completed'] = True
            print(f"Task marked as completed: {self.tasks[task_index - 1]['description']}")
        else:
            print("Invalid task index.")


def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List Menu:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '3':
            task_index = int(input("Enter task index to delete: "))
            todo_list.delete_task(task_index)
        elif choice == '4':
            task_index = int(input("Enter task index to mark as completed: "))
            todo_list.mark_as_completed(task_index)
        elif choice == '5':
            print("Exiting the Todo List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
