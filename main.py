import os
from dotenv import load_dotenv
import users
import tasks

# Load environment variables
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

def main():
    print("=== Welcome to Task Manager App ===")
    current_user = authenticate_flow()
    task_manager(current_user)

def authenticate_flow():
    """Handles sign in / sign up loop"""
    while True:
        print("\n1. Sign In")
        print("2. Sign Up")
        choice = users.get_user_choice()

        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if users.authenticate_user(username, password):
                print("✅ Sign in successful!")
                return username
            else:
                print("❌ Invalid username or password. Try again.")

        elif choice == "2":
            username = input("Choose a username: ")
            password = input("Choose a password: ")
            if users.add_user(username, password):
                print("✅ Sign up successful!")
                return username
            else:
                print("❌ Username already exists. Try again.")

        else:
            print("Invalid choice. Please enter 1 or 2.")

def task_manager(current_user):
    """Main task management loop"""
    while True:
        print("\n--- Task Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task_flow(current_user)
        elif choice == "2":
            view_tasks_flow(current_user)
        elif choice == "3":
            complete_task_flow(current_user)
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_task_flow(current_user):
    task_name = input("Enter task name: ")
    task_desc = input("Enter task description: ")
    if tasks.add_task(current_user, task_name, task_desc):
        print(f"✅ Task '{task_name}' added successfully!")
    else:
        print("❌ Failed to add task (duplicate or user not found).")

def view_tasks_flow(current_user):
    all_tasks = tasks.view_tasks(current_user)
    if not all_tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for task_id, task_info in all_tasks.items():
            status = "✔️ Completed" if task_info.get("completed") else "⏳ Pending"
            print(f"ID: {task_id} | Name: {task_info['name']} | Desc: {task_info['description']} | Status: {status}")

def complete_task_flow(current_user):
    task_id = input("Enter task ID to mark as completed: ")
    if tasks.complete_task(current_user, task_id):
        print(f"✅ Task {task_id} marked as completed!")
    else:
        print("❌ Task not found or already completed.")

if __name__ == "__main__":
    main()


