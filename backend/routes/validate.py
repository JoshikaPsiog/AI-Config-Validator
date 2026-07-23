from fastapi import APIRouter
import subprocess
import os

from ai.ollama_service import ask_ollama
from ai.prompt_builder import build_validation_prompt

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
    print("Terraform files:", tf_files)
    print("Validating:", file_path)
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

    # PASS
    if result.returncode == 0:
        return {
            "status": "PASS",
            "output": result.stdout
        }

    # FAIL → Ask Ollama
    validation_output = result.stdout + "\n" + result.stderr

    prompt = build_validation_prompt(validation_output)

    ai_response = ask_ollama(prompt)

    return {
        "status": "FAIL",
        "output": result.stdout,
        "error": result.stderr,
        "ai_explanation": ai_response
    }