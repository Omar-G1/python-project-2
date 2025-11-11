# Task Manager API 🚀

A FastAPI-based REST API for managing tasks with user authentication (JWT) and PostgreSQL database.

## Features 

- User signup & login with JWT authentication
- Create, read, and delete tasks per user
- PostgreSQL database integration with SQLAlchemy
- Password hashing with bcrypt
- Automatic interactive API docs at `/docs`

## Project Structure 
project/
            ├── main.py # FastAPI app & routes
            ├── database.py # SQLAlchemy models (User, Task) & DB setup
            ├── schemas.py # Pydantic request/response models
            ├── auth.py # JWT & password helpers
            ├── requirements.txt # Python dependencies
            ├── README.md # This file


- Python 3.9+
- PostgreSQL 16+ installed and running
- A database named `taskmanager` created in PostgreSQL


## Prerequisites 📋

- Python 3.9+
- PostgreSQL 16+ installed and running
- A database named `taskmanager` created in PostgreSQL

## Setup Instructions 🛠️

### Step 1: Navigate to your project folder


### Step 2: Create a virtual environment
python -m venv .venv

### Step 3: Activate the virtual environment
**Windows (PowerShell):**
..venv\Scripts\Activate.ps1

**Linux/MacOS (Terminal):**
source .venv/bin/activate

### Step 4: Install dependencies
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-jose[cryptography] passlib[bcrypt] python-dotenv bcrypt


### Step 5: Set up PostgreSQL database

Open pgAdmin or use CMD/PowerShell and type:


Then in PostgreSQL, type:


### Step 6: Configure database connection

Open `database.py` and find this line:

DATABASE_URL = "postgresql://postgres:pass@localhost:5432/taskmanager"

### Step 7: Run the API
python -m uvicorn main:app --reload

### Step 8: Access the API
Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation.


You'll see the interactive Swagger UI where you can test all endpoints! 🎉

## API Endpoints 📡

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/signup` | Create new user | No |
| POST | `/login` | Get JWT token | No |
| POST | `/tasks` | Create a task | Yes |
| GET | `/tasks` | List your tasks | Yes |
| DELETE | `/tasks/{task_id}` | Delete a task | Yes |

## How to Use the API 📖

### 1️⃣ Signup

Go to `/docs` → Click **POST /signup** → **Try it out**

Fill in:

Username: your_username
: your_password

Click **Execute**

### 2️⃣ Login

Click **POST /login** → **Try it out**

Fill in:
- username: `ahmed`
- password: `mypassword123`

Click **Execute** → Copy the `access_token` 🔐

### 3️⃣ Authorize the UI

Click the **🔒 Authorize** button (top right)

Bearer YOUR_ACCESS_TOKEN_HERE


Click **Authorize** → **Close** ✅

### 4️⃣ Add a Task

Click **POST /tasks** → **Try it out**

Fill in:
{
"name": "Learn FastAPI",
"description": "Build and deploy REST API"
}

Click **Execute** ✅

### 5️⃣ View Your Tasks

Click **GET /tasks** → **Execute**

You'll see all your tasks! 📋

### 6️⃣ Delete a Task

Click **DELETE /tasks/{task_id}** → **Try it out**

Enter the task ID from step 4

Click **Execute** ✅

## Troubleshooting 🔧

**Error: "Could not import module 'main'"**
- Make sure you're in the correct folder with `main.py`
- Check for typos in your Python files

**Error: "password authentication failed"**
- Verify your PostgreSQL password is correct in `database.py`

**Error: "uvicorn not recognized"**
- Activate your virtual environment first:
..venv\Scripts\Activate.ps1


**API not responding**
- Make sure PostgreSQL is running
- Check if port 8000 is free (no other app using it)



## Technologies Used 🛠️

- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - Database ORM
- **PostgreSQL** - Database
- **Pydantic** - Data validation
- **JWT** - Authentication
- **bcrypt** - Password hashing
- container - docker



