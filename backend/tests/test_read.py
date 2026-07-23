from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_file():

    response = client.get("/read/sample.tf")

    assert response.status_code == 200

def test_tf_files():

    response = client.get("/terraform-files")

    assert response.status_code == 200