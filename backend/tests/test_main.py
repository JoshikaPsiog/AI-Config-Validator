from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_ai():
    response = client.get("/ai-test")
    assert response.status_code == 200

def test_ollama():
    response = client.get("/ollama-test")
    assert response.status_code == 200