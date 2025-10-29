
import json
import os
import bcrypt

# --- Data Management ---
def load_users(filepath="users.json"):
    """Load users from a JSON file. Return empty dict if file doesn't exist."""
    if not os.path.exists(filepath):
        return {}
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading users: {e}")
        return {}

def save_users(users_db, filepath="users.json"):
    """Save users dictionary to a JSON file."""
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(users_db, file, indent=4)
    except IOError as e:
        print(f"Error saving users: {e}")

# --- Authentication Logic ---
def authenticate_user(users_db, username, password):
    """Check if username exists and password matches the stored hash."""
    if username not in users_db:
        return False
    stored_hash = users_db[username]["password"]
    return bcrypt.checkpw(password.encode("utf-8"), stored_hash.encode("utf-8"))

def add_user(users_db, username, password):
    """Add a new user with a hashed password. Return (True, None) on success, or (False, reason) on failure."""
    if not username or not password:
        return False, "Username and password cannot be empty."
    if username in users_db:
        return False, "Username already exists."
    
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    users_db[username] = {
        "password": hashed.decode("utf-8"),
        "tasks": {}
    }
    save_users(users_db)
    return True, None

# --- User Interface ---
def get_user_choice():
    """Prompt user to choose option 1 or 2."""
    while True:
        choice = input("Choose an option (1 or 2): ").strip()
        if choice in ("1", "2"):
            return choice
        print("Invalid choice. Please enter 1 or 2.")



