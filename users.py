import json
import os
def load_users():
    if not os.path.exists("users.json"):
        return {}
    with open("users.json", "r") as file:
        return json.load(file)

def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users_db, file, indent=4)
        
def get_user_choice():
    return input("Choose an option (1 or 2): ")

def authenticate_user(username, password):
    return users_db.get(username) == password

def add_user(username, password):
    if username in users_db:
        return False
    users_db[username] = password
    save_users(users_db)
    return True  

users_db = load_users()
user_tasks = {}  # {username: [ {name:..., description:...}, ... ] }

def add_task(username, name, description):
   
    if username not in user_tasks:
        user_tasks[username] = []
    user_tasks[username].append({"name": name, "description": description})

def view_tasks(username):
    return user_tasks.get(username, [])
