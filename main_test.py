import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_signup():
    response = client.post("/signup", json={
        "username": "testuser",
        "password": "testpass123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login():
    # First signup
    client.post("/signup", json={
        "username": "testuser2",
        "password": "pass123"
    })
    
    # Then login
    response = client.post("/login", json={
        "username": "testuser2",
        "password": "pass123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_create_task_unauthorized():
    response = client.post("/tasks", json={
        "name": "Test",
        "description": "Test"
    })
    assert response.status_code == 401  # Should require auth
