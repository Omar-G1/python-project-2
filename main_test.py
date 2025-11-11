import pytest
from fastapi.testclient import TestClient
from main import app
import random

client = TestClient(app)

def generate_unique_username():
    """Generate unique username for each test"""
    return f"testuser{random.randint(1000, 9999)}"

def test_signup():
    username = generate_unique_username()
    response = client.post("/signup", json={
        "username": username,
        "password": "testpass123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login():
    # First signup
    username = generate_unique_username()
    client.post("/signup", json={
        "username": username,
        "password": "pass123"
    })
    
    # Then login
    response = client.post("/login", json={
        "username": username,
        "password": "pass123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_create_task_unauthorized():
    """Test creating task without auth token"""
    response = client.post("/tasks", json={
        "name": "Test",
        "description": "Test"
    })
    assert response.status_code == 401  # Should require auth

def test_create_task_authorized():
    """Test creating task WITH auth token"""
    # Signup and get token
    username = generate_unique_username()
    signup_response = client.post("/signup", json={
        "username": username,
        "password": "pass123"
    })
    token = signup_response.json()["access_token"]
    
    # Create task with token
    response = client.post(
        "/tasks",
        json={"name": "Test Task", "description": "Test Description"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200

def test_get_tasks_unauthorized():
    """Test getting tasks without auth"""
    response = client.get("/tasks")
    assert response.status_code == 401

def test_get_tasks_authorized():
    """Test getting tasks WITH auth"""
    # Signup and get token
    username = generate_unique_username()
    signup_response = client.post("/signup", json={
        "username": username,
        "password": "pass123"
    })
    token = signup_response.json()["access_token"]
    
    # Get tasks
    response = client.get(
        "/tasks",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)

