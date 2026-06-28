import datetime
import json
import sys


# Functions
def save_data(data, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


file_path = "tasks.json"
# Try to open existing JSON file, create new if not exists
try:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    data = []
    save_data(data, file_path)
# Commands: add, update <id> <description>, delete <id>, mark-in-progress <id>, mark-done <id>, list, list done, list todo, list in-progress

quick_start = """
    Quick Start Guide

    # Adding a new task
    task-cli add "Buy groceries"
    # Output: Task added successfully (ID: 1)

    # Updating and deleting tasks
    task-cli update 1 "Buy groceries and cook dinner"
    task-cli delete 1

    # Marking a task as in progress or done
    task-cli mark-in-progress 1
    task-cli mark-done 1

    # Listing all tasks
    task-cli list

    # Listing tasks by status
    task-cli list done
    task-cli list todo
    task-cli list in-progress
    """

script_name = sys.argv[0]
if len(sys.argv) < 2:
    print(quick_start)
else:
    command = sys.argv[1]
    match command:
        case "add":
            data.append(
                {
                    "id": len(data) + 1,
                    "description": sys.argv[2],
                    "status": "todo",
                    "createdAt": datetime.datetime.now().strftime(
                        "%d/%m/%y at %I:%M%p"
                    ),
                    "updatedAt": datetime.datetime.now().strftime(
                        "%d/%m/%y at %I:%M%p"
                    ),
                }
            )
            save_data(data, file_path)
            print(f'Added "{sys.argv[2]}" to list.')
        case "update":
            for i in data:
                if i["id"] == int(sys.argv[2]):
                    i["description"] = sys.argv[3]
                    i["updatedAt"] = datetime.datetime.now().strftime(
                        "%d/%m/%y at %I:%M%p"
                    )
            save_data(data, file_path)
            print(f"Updated task {sys.argv[2]}.")
        case "delete":
            for i in data:
                if i["id"] == int(sys.argv[2]):
                    for j in data:
                        if j["id"] > i["id"]:
                            j["id"] -= 1
                    data.remove(i)
            save_data(data, file_path)
            print(f"Deleted task {sys.argv[2]}")
        case "mark-in-progress":
            for i in data:
                if i["id"] == int(sys.argv[2]):
                    i["status"] = "in-progress"
            save_data(data, file_path)
            print(f"Marked task {sys.argv[2]} 'in-progress'")
        case "mark-done":
            for i in data:
                if i["id"] == int(sys.argv[2]):
                    i["status"] = "done"
            save_data(data, file_path)
            print(f"Marked task {sys.argv[2]} 'done'")
        case "list":
            if len(sys.argv) == 2:
                for i in data:
                    print(f"{i['id']}: {i['description']}")
            else:
                for i in data:
                    if sys.argv[2] == i["status"]:
                        print(i["description"])
        case _:
            print("Please enter a valid command.")
            print(quick_start)
