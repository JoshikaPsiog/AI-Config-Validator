from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_upload():
    files = {
        "file": (
            "sample.tf",
            b'resource "aws_s3_bucket" "demo" {}'
        )
    }

    response = client.post("/upload", files=files)

    assert response.status_code == 200
    assert response.json()["status"] == "success"