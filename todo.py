import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)


def show_tasks(tasks):
    if not tasks:
        print("\n  nothing on the list yet.\n")
        return

    print("\n  your tasks:")
    print("  " + "-" * 30)
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else "○"
        label  = task["task"]
        if task["done"]:
            label = f"\033[90m{label}\033[0m"  
        print(f"  {i}. [{status}] {label}")
    print()


def add_task(tasks):
    name = input("  task name: ").strip()
    if not name:
        print("  can't add an empty task.\n")
        return
    tasks.append({"task": name, "done": False})
    save_tasks(tasks)
    print(f"  added: \"{name}\"\n")


def mark_done(tasks):
    show_tasks(tasks)
    if not tasks:
        return

    raw = input("  task number to mark done: ").strip()
    if not raw.isdigit():
        print("  that's not a number.\n")
        return

    n = int(raw)
    if not (1 <= n <= len(tasks)):
        print("  number out of range.\n")
        return

    if tasks[n - 1]["done"]:
        print("  already done.\n")
        return

    tasks[n - 1]["done"] = True
    save_tasks(tasks)
    print(f"  marked done: \"{tasks[n - 1]['task']}\"\n")


def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return

    raw = input("  task number to delete: ").strip()
    if not raw.isdigit():
        print("  that's not a number.\n")
        return

    n = int(raw)
    if not (1 <= n <= len(tasks)):
        print("  number out of range.\n")
        return

    removed = tasks.pop(n - 1)
    save_tasks(tasks)
    print(f"  deleted: \"{removed['task']}\"\n")


def main():
    tasks = load_tasks()

    print("\n  === to-do list ===")

    while True:
        print("  1. add task")
        print("  2. view tasks")
        print("  3. mark done")
        print("  4. delete task")
        print("  5. quit")

        choice = input("\n  > ").strip()
        print()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("  bye.\n")
            break
        else:
            print("  not a valid option.\n")


main()