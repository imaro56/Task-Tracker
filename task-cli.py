import json
import sys
from datetime import datetime


def main():
    filename = 'database.json'
    database = open_json(filename)
    input_str = sys.argv[1:]

    operations(database, input_str)
    save_json(database, filename)


# def operation_rules(operation):
#     rules = [
#         {'add':{
#             'func': add_op,
#             'min_args': 1,
#             'max_args': 1,
#             'help': 'Adds a task to your list. Structure: add "description". Example: add "Go to the gym" '
#
#         }},
#         {'update':{
#             'func': update,
#             'min_args': 2,
#             'max_args': 2,
#             'help': 'Updates a task in your list. Structure: update id "description". Example: update 1 "Go to school"'
#         }},
#         {'delete':{
#             'func': delete,
#             'min_args': 1,
#             'max_args': 1,
#             'help': 'Removes a task from your list. Structure: delete id'
#         }},
#         {'mark-in-progress':{
#             'func': mark_in_progress,
#             'min_args': 1,
#             'max_args': 1,
#             'help': 'Change status of the task to "in-progress". Structure: mark-in-progress id'
#         }},
#         {'mark-done':{
#             'func': mark_done,
#             'min_args': 1,
#             'max_args': 1,
#             'help': 'Change status of the task to "done". Structure: mark-done id'
#         }},
#         {'mark-todo':{
#             'func': mark_to_do,
#             'min_args': 1,
#             'max_args': 1,
#             'help': 'Change status of the task to "to-do". Structure: mark-to-do id'
#         }},
#         {'list':{
#             'func': print_list,
#             'min_args': 0,
#             'max_args': 1,
#             'possible_args': ['to-do','in-progress','done'],
#             'help': 'Prints list to the console, you can choose if you want to print tasks with certain status. Structure: list status(optional). Example1: list. Example2: list done'
#         }},
#
#
#     ]

def operations(database, args):
    command = args[0]
    match str(command):
        case 'add':
            if len(args)<2:
                return
            description = args[1]
            add_op(database, description)
        case 'update':
            if len(args)<3:
                return
            try:
                task_id = int(args[1])
            except ValueError:
                return
            description = args[2]
            update(database, task_id, description)
        case 'delete':
            try:
                task_id = int(args[1])
            except (ValueError, IndexError):
                return
            delete(database, task_id)
        case 'list':
            try:
                list_type = args[1]
            except IndexError:
                list_type = ''
            print_list(database, list_type)
        case 'mark-in-progress' | 'mark-done' | 'mark-todo':
            try:
                task_id = int(args[1])
            except (ValueError, IndexError):
                return
            mark(database, command, task_id)


def add_op(database, description):
    if database:
        task_id = database[-1]['id'] + 1
    else:
        task_id = 1

    database.append(
        {'id': task_id, 'description': description, 'status': 'todo', 'createdAt': datetime.now().strftime("%D %H:%M"),
         'updatedAt': datetime.now().strftime("%D %H:%M")})

    print(f'Task added successfully (ID: {task_id})')


def update(database, task_id, new_description):
    for i in range(len(database)):
        if database[i]['id'] == task_id:
            database[i]['description'] = new_description
            database[i]['updatedAt'] = datetime.now().strftime("%D %H:%M")
            print(f'Task updated successfully (ID: {task_id})')
            return
    print(f'Task with ID: {task_id}, does not exist!')


def delete(database, task_id):
    flag = False
    for i in range(len(database)):
        if database[i]['id'] == task_id:
            database.pop(i)
            flag = True
            break
    if flag:
        print(f'Task deleted successfully (ID: {task_id})')
    else:
        print(f'Task with ID: {task_id}, does not exist!')


def print_list(database, list_type):
    is_tasks = False
    string_list = f'{'-' * 100}\n|{"ID":^4}|{"Description":^40}|{"Status":^14}|{"Created At":^18}|{"Updated At":^18}|\n{'-' * 100}\n'
    for task in database:
        if list_type in ('todo', 'in-progress', 'done') and task['status'] != list_type:
            continue
        is_tasks = True
        string_list += f'|{task['id']:^4}|{task['description'][:38]:^40}|{task['status']:^14}|{task['createdAt']:^18}|{task['updatedAt']:^18}|\n{'-' * 100}\n'

    if is_tasks:
        print(string_list)
    else:
        print(f"List {"of " + list_type + " tasks " if list_type else ''}is empty(")


def mark(database, command, task_id):
    status = ''
    match command:
        case 'mark-in-progress':
            status = 'in-progress'
        case 'mark-done':
            status = 'done'
        case 'mark-todo':
            status = 'todo'
    if status == '':
        return
    for i in range(len(database)):
        if database[i]['id'] == task_id:
            database[i]['status'] = status
            database[i]['updatedAt'] = datetime.now().strftime("%D %H:%M")
            print(f'Task marked as {status} successfully (ID: {task_id})')
            return
    print(f'Task with ID: {task_id}, does not exist!')


def open_json(name):
    try:
        with open(name, mode="r", encoding="utf-8") as read_file:
            database = json.load(read_file)
    except (json.JSONDecodeError, FileNotFoundError):
        with open(name, mode="w", encoding="utf-8") as write_file:
            database = []
            json.dump([], write_file, indent=4)
    return database


def save_json(database, name):
    with open(name, mode="w", encoding="utf-8") as write_file:
        json.dump(database, write_file, indent=4)


def read_cli():
    pass


if __name__ == '__main__':
    main()
