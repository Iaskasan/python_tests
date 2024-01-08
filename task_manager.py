def add_task(tasks, description):
    task = {"description": description, "completed": False}
    tasks.append(task)

def display_tasks(tasks):
    for i, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i + 1}. {task['description']} [{status}]")

def mark_task_completed(tasks, task_number):
    if 0 <= task_number - 1 < len(tasks):
        tasks[task_number - 1]["completed"] = True

def delete_task(tasks, task_number):
    if 0 <= task_number - 1 < len(tasks):
        del tasks[task_number - 1]

# Liste pour stocker les tâches
tasks = []

# Boucle principale de l'application
while True:
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        task_desc = input("Enter task description: ")
        add_task(tasks, task_desc)
    elif choice == "2":
        display_tasks(tasks)
    elif choice == "3":
        task_num = int(input("Enter task number to mark as completed: "))
        mark_task_completed(tasks, task_num)
    elif choice == "4":
        task_num = int(input("Enter task number to delete: "))
        delete_task(tasks, task_num)
    elif choice == "5":
        break
