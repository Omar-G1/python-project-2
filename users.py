
import json
import os
import bcrypt

users_db = load_users()


def load_users():
    if not os.path.exists("users.json"):
        return {}
    with open("users.json", "r") as file:
        return json.load(file)


def save_users(users_db):  
    with open("users.json", "w") as file:
        json.dump(users_db, file, indent=4)
        
def get_user_choice():
    while True:
        try:
            choice = input("Choose an option (1 or 2): ")
            if choice in ["1", "2"]:
                return choice
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
            continue


def authenticate_user(users_db, username, password):  # Added users_db here!
    if username in users_db and bcrypt.checkpw(password.encode('utf-8'), users_db[username]["password"].encode('utf-8')):
        return True
    return False

def add_user(users_db, username, password):  # Added users_db here too!
    if username in users_db:
        return False
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    users_db[username] = {"password": hashed_password.decode('utf-8'), "tasks": {}}
    save_users(users_db)
    return True


