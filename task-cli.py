import json
import sys
from datetime import datetime


def operations(args, todo_list):
    command = args[0]
    if command == 'add':
        description = args[1]
        add_op(description, todo_list)
    elif command == 'update':
        task_id = int(args[1])
        description = args[1]
        update(task_id,description,todo_list)


def add_op(description, todo_list):
    task_id = todo_list[-1]['id'] + 1
    todo_list.append(
        {'id': task_id,
         'description': description,
         'status': 'todo',
         'createdAt': datetime.now().strftime("%D %H:%M"),
         'updatedAt': datetime.now().strftime("%D %H:%M")
        })

    with open("todo_list.json", mode="w", encoding="utf-8") as write_file:
        json.dump(todo_list, write_file, indent=4)

    print(f'Task added successfully (ID: {task_id})')


def update(task_id, new_description, todo_list):
    flag = False
    for i in range(len(todo_list)) :
        if todo_list[i]['id'] == task_id:
            todo_list[i]['description'] = new_description
            todo_list[i]['updatedAt'] = datetime.now().strftime("%D %H:%M")
            flag = True
            break
    if flag:
        with open("todo_list.json", mode="w", encoding="utf-8") as write_file:
            json.dump(todo_list, write_file, indent=4)

        print(f'Task updated successfully (ID: {task_id})')
    else:
        print(f'Task with ID: {task_id}, does not exist!')


def open_json():
    try:
        with open("todo_list.json", mode="r", encoding="utf-8") as read_file:
            todo_list = json.load(read_file)
    except (json.JSONDecodeError, FileNotFoundError):
        with open("todo_list.json", mode="w", encoding="utf-8") as write_file:
            todo_list = []
            json.dump([], write_file, indent=4)
    return todo_list


if __name__ == '__main__':
    args = sys.argv[1:]

    array = open_json()

    if len(args) == 0:
        while True:
            string = input('Enter the command(help for details): ')
            operations(string.split(), array)
    else:
        operations(args, array)
