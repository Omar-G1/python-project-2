tasks = {}
user_tasks = {}

def task_name_exists(name):
    return any(task['name'] == name for task in tasks.values())


def add_task(username, name, description):
    if username not in user_tasks:
        user_tasks[username] = []
    user_tasks[username].append({"name": name, "description": description})

def view_tasks(username):
    return user_tasks.get(username, [])


def view_tasks(username):
    return user_tasks.get(username, [])