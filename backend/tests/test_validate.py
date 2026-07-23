from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_validate():

    response = client.post("/validate")

    assert response.status_code == 200