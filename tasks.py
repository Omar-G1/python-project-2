import users  

def add_task(username, name, description):

    if username not in users.users_db:
        print("User not found.")
        return False
    
    user_tasks = users.users_db[username].setdefault("tasks", {})
    if any(t["name"] == name for t in user_tasks.values()):
        print("Task name already exists for this user.")
        return False
    
    task_id = max(user_tasks.keys(), default=0) + 1
    user_tasks[task_id] = {"name": name, "description": description}
   
    users.save_users(users.users_db)
    return True

def view_tasks(username):
    if username not in users.users_db:
        return {}
    return users.users_db[username].get("tasks", {})
