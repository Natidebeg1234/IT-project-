tasks = ["physics assignment", "math test", "bio lab-report"]
completed_tasks = []


def display_tasks():
    print("===== TO-DO LIST =====")
    number = 1

    for task in tasks:
        print(number, ".", task)
        number += 1

    if tasks == []:
        print("No tasks yet.")
    print()


def display_completed_tasks():
    print("===== COMPLETED TASKS =====")
    number = 1

    for task in completed_tasks:
        print(number, ".", task)
        number += 1

    if completed_tasks == []:
        print("No completed tasks yet.")
    print()


def add_task():
    name = input("Enter new task: ")
    tasks.append(name)
    print("Task added!")
    print()


def remove_task():
    display_tasks()

    if tasks == []:
        return

    index = int(input("Enter task number to remove: "))
    index = index - 1

    if index >= 0:
        tasks.pop(index)
        print("Task removed!")
    else:
        print("Invalid task number!")
    print()


def edit_task():
    display_tasks()

    if tasks == []:
        return

    index = int(input("Enter task number to edit: "))
    index = index - 1

    if index >= 0:
        tasks[index] = input("Enter new task name: ")
        print("Task updated!")
    else:
        print("Invalid task number!")
    print()


def complete_task():
    display_tasks()

    if tasks == []:
        return

    index = int(input("Enter task number to complete: "))
    index = index - 1

    if index >= 0:
        task = tasks.pop(index)
        completed_tasks.append(task)
        print("Task marked as completed!")
    else:
        print("Invalid task number!")
    print()


def main():
    print("===== SIMPLE TO-DO LIST =====")

    while True:
        display_tasks()
        display_completed_tasks()

        print("MENU")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Edit Task")
        print("4. Complete Task")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            edit_task()
        elif choice == "4":
            complete_task()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")
            print()


main()
