tasks = []


def show_menu():
    print("\nApplication TODO list")
    print("1. Create a task")
    print("2. Edit a task")
    print("3. Delete a task")
    print("4. Filter task")
    print("5. Sort tasks")
    print("0. Exit")


def print_tasks():
    if not tasks:
        print("No task available")
    else:
        print("\nTasks:")
        for task in tasks:
            print(f"- Name: {task['name']}, Priority: {task['priority']}, Category: {task['category']}")


def create_task(name, priority, category):
    global tasks
    task = {"name": name, "priority": priority, "category": category}
    tasks.append(task)
    print(f"Task '{name}' added successfully! ")
    print_tasks()


def edit_task(old_name, new_name, new_priority, new_category):
    global tasks
    found = False
    for task in tasks:
        if task['name'] == old_name:
            task['name'] = new_name
            task['priority'] = new_priority
            task['category'] = new_category
            found = True
            print(f"Task '{old_name}' has been updated successfully!")
    if not found:
        print("Task not found")
    else:
        print_tasks()


def delete_task(name):
    global tasks
    found = False
    new_tasks = []
    for task in tasks:
        if task['name'] != name:
            tasks.append(task)
        else:
            found = True
    tasks = new_tasks
    if found:
        print(f"Task '{name}' deleted.")
        print_tasks()
    else:
        print("Task not found.")


def filter_tasks(key, value):
    found = False
    print("\nFiltered tasks: ")
    for task in tasks:
        if task.get(key) == value:
            found = True
            print(f"- Name: {task['name']}, Priority: {task['priority']}, Category: {task['category']}")
    if not found:
        print("No matching task found!")


def sort_tasks(key):
    global tasks
    if key not in ["name", "priority", "category"]:
        print("Invalid sort key. Please use 'name', 'priority', or 'category'.")
    priority_order = {"low": 1, "medium": 2, "high": 3}
    for i in range(len(tasks) - 1):
        print(i)
        for j in range(len(tasks) - i - 1):
            print(j)
            if key == "priority":
                print(f"if {priority_order[tasks[j][key]]} > {priority_order[tasks[j + 1][key]]}")
                if priority_order[tasks[j][key]] > priority_order[tasks[j + 1][key]]:

                    tasks[j], tasks[j + 1] = tasks[j + 1], tasks[j]
                else:
                    print(f"if {tasks[j][key]} > {tasks[j + 1][key]}")
                    if tasks[j][key] > tasks[j + 1][key]:
                        print(f"{tasks[j], tasks[j + 1]} = {tasks[j + 1], tasks[j]}")
                        tasks[j], tasks[j + 1] = tasks[j + 1], tasks[j]
    print(f"Tasks sorted by {key}:")
    print_tasks()


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter task name: ")
            priority = input("Enter priority (low/medium/high): ")
            category = input("Enter category: ")
            create_task(name, priority, category)
        elif choice == '2':
            old_name = input("Enter old task name: ")
            new_name = input("Enter new task name: ")
            new_priority = input("Enter new priority (low/medium/high): ")
            new_category = input("Enter new category: ")
            edit_task(old_name, new_name, new_priority, new_category)
        elif choice == '3':
            name = input("Enter task name to delete: ")
            delete_task(name)
        elif choice == '4':
            key = input("Enter filter key (name/priority/category): ")
            value = input("Enter filter value: ")
            filter_tasks(key, value)
        elif choice == '5':
            key = input("Enter sort key (name/priority/category): ")
            sort_tasks(key)
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please choose again.")


main()
