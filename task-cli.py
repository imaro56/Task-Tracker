import json
import sys
from datetime import datetime


def operations(args, todo_list):
    command = args[0]
    match str(command):
        case 'add':
            description = args[1]
            add_op(description, todo_list)
        case 'update':
            task_id = int(args[1])
            description = args[2]
            update(task_id, description, todo_list)
        case 'delete':
            task_id = int(args[1])
            delete(task_id, todo_list)
        case 'list':
            try:
                list_type = args[1]
            except IndexError:
                list_type = ''
            print_list(todo_list, list_type)
        case 'mark-in-progress' | 'mark-done' | 'mark-todo':
            task_id = int(args[1])
            mark(todo_list, command.replace('mark-', ''), task_id)


def add_op(description, todo_list):
    if todo_list:
        task_id = todo_list[-1]['id'] + 1
    else:
        task_id = 1

    todo_list.append(
        {'id': task_id, 'description': description, 'status': 'todo', 'createdAt': datetime.now().strftime("%D %H:%M"),
         'updatedAt': datetime.now().strftime("%D %H:%M")})

    print(f'Task added successfully (ID: {task_id})')


def update(task_id, new_description, todo_list):
    for i in range(len(todo_list)):
        if todo_list[i]['id'] == task_id:
            todo_list[i]['description'] = new_description
            todo_list[i]['updatedAt'] = datetime.now().strftime("%D %H:%M")
            print(f'Task updated successfully (ID: {task_id})')
            return
    print(f'Task with ID: {task_id}, does not exist!')


def delete(task_id, todo_list):
    flag = False
    for i in range(len(todo_list)):
        if todo_list[i]['id'] == task_id:
            todo_list.pop(i)
            flag = True
            break
    if flag:
        print(f'Task deleted successfully (ID: {task_id})')
    else:
        print(f'Task with ID: {task_id}, does not exist!')


def print_list(todo_list, list_type):
    is_tasks = False
    string_list = f'{'-' * 100}\n|{"ID":^4}|{"Description":^40}|{"Status":^14}|{"Created At":^18}|{"Updated At":^18}|\n{'-' * 100}\n'
    for task in todo_list:
        if list_type in ('todo', 'in-progress', 'done') and task['status'] != list_type:
            continue
        is_tasks = True
        string_list += f'|{task['id']:^4}|{task['description'][:38]:^40}|{task['status']:^14}|{task['createdAt']:^18}|{task['updatedAt']:^18}|\n{'-' * 100}\n'

    if is_tasks:
        print(string_list)
    else:
        print(f"List {"of " + list_type + " tasks " if list_type else ''}is empty(")


def mark(todo_list, status, task_id):
    for i in range(len(todo_list)):
        if todo_list[i]['id'] == task_id:
            todo_list[i]['status'] = status
            todo_list[i]['updatedAt'] = datetime.now().strftime("%D %H:%M")
            print(f'Task marked as {status} successfully (ID: {task_id})')
            return
    print(f'Task with ID: {task_id}, does not exist!')


def open_json(name):
    try:
        with open(name, mode="r", encoding="utf-8") as read_file:
            todo_list = json.load(read_file)
    except (json.JSONDecodeError, FileNotFoundError):
        with open(name, mode="w", encoding="utf-8") as write_file:
            todo_list = []
            json.dump([], write_file, indent=4)
    return todo_list


def save_json(name, todo_list):
    with open(name, mode="w", encoding="utf-8") as write_file:
        json.dump(todo_list, write_file, indent=4)


if __name__ == '__main__':
    filename = 'todo_list.json'
    line = sys.argv[1:]

    array = open_json(filename)

    operations(line, array)
    save_json(filename, array)
