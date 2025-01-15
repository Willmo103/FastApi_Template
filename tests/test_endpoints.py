# tests/test_endpoints.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI Template!"}

def test_uptime():
    response = client.get("/api/v1/uptime")
    assert response.status_code == 200
    assert response.json()["status"] == "up"

def test_generate_api_key():
    response = client.post("/api/v1/generate-api-key", json={"owner": "test_user"})
    assert response.status_code == 200
    assert "key" in response.json()

# Additional tests can be added here
