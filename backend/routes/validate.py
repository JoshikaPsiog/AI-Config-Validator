from fastapi import APIRouter
import subprocess
import os

router = APIRouter()

# backend folder
BACKEND_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# project root
PROJECT_ROOT = os.path.dirname(BACKEND_DIR)

UPLOAD_FOLDER = os.path.join(PROJECT_ROOT, "uploads")
POLICY_FOLDER = os.path.join(PROJECT_ROOT, "policies")


@router.post("/validate")
def validate():

    if not os.path.exists(UPLOAD_FOLDER):
        return {
            "status": "ERROR",
            "message": f"Uploads folder not found: {UPLOAD_FOLDER}"
        }

    tf_files = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith(".tf")]

    if not tf_files:
        return {
            "status": "ERROR",
            "message": "No Terraform file found in uploads."
        }

    file_path = os.path.join(UPLOAD_FOLDER, tf_files[0])

    result = subprocess.run(
        [
            "conftest",
            "test",
            file_path,
            "--policy",
            POLICY_FOLDER
        ],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT
    )

    if result.returncode == 0:
        return {
            "status": "PASS",
            "output": result.stdout
        }

    return {
        "status": "FAIL",
        "output": result.stdout,
        "error": result.stderr
    }