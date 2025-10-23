import tasks
import users

current_user = None

while True:
    print("Task Manager App is running...")  # main.py
    try:
        print("1. sign in")
        print("2. sign up")
        choice = users.get_user_choice()

        if choice == "1":
            enter_username = input("Enter your username: ")
            enter_password = input("Enter your password: ")
            print(f"Signing in {enter_username}...")

            if users.authenticate_user(enter_username, enter_password):
                print("Sign in successful!")
                current_user = enter_username
                break
            else:
                print("Invalid username or password. Please try again.")

        elif choice == "2":
            new_username = input("Enter a new username: ")
            new_password = input("Enter a new password: ")
            print(f"Signing up {new_username}...")

            if users.add_user(new_username, new_password):
                print("Sign up successful!")
                current_user = new_username
                break
            else:
                print("Username already exists. Please try again.")

        else:
            print("Invalid choice. Please try again.")

    except Exception as e:
        print(f"An error occurred: {e}")
    continue


while True:
    print("1. Add Task")
    print("2. View Tasks")
    task_choice = input("Choose an option (1 or 2): ")

    if task_choice == "1":
        task_name = input("Enter task name: ")
        task_desc = input("Enter task description: ")
        # Fix: Check the return value of add_task to handle errors (e.g., duplicate or user not found)
        if tasks.add_task(current_user, task_name, task_desc):
            print(f"Task '{task_name}' added successfully!")
        else:
            print("Failed to add task. (User not found or duplicate name)")

    elif task_choice == "2":
        all_tasks = tasks.view_tasks(current_user)
        if not all_tasks:
            print("No tasks available.")
        else:
            # Fix: Now that view_tasks returns a dict {id: task_info}, .items() works correctly with task IDs
            for task_id, task_info in all_tasks.items():
                print(f"ID: {task_id}, Name: {task_info['name']}, Description: {task_info['description']}")

    else:
        print("Invalid choice. Please try again.")

    continue_option = input("Do you want to continue? (yes/no): ")
    if continue_option.lower() != "yes":
        print("Exiting Task Manager App. Goodbye!")
        break
    print("Task Manager App is running...") 
