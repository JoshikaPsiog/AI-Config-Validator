from fastapi import APIRouter
import subprocess
import os

from ai.groq_service import ask_groq
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

    # Check uploads folder
    if not os.path.exists(UPLOAD_FOLDER):
        return {
            "status": "ERROR",
            "message": f"Uploads folder not found: {UPLOAD_FOLDER}"
        }

    # Get all IaC files
    iac_files = [
        f for f in os.listdir(UPLOAD_FOLDER)
        if f.endswith(".tf") or f.endswith(".bicep")
    ]

    if not iac_files:
        return {
            "status": "ERROR",
            "message": "No IaC files found in uploads folder."
        }

    results = []
    passed = 0
    failed = 0

    # Validate every file
    for file_name in iac_files:

        file_path = os.path.join(UPLOAD_FOLDER, file_name)

        print(f"Validating: {file_path}")

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

            passed += 1

            results.append({
                "file": file_name,
                "status": "PASS",
                "output": result.stdout.strip()
            })

        # FAIL
        else:

            failed += 1

            validation_output = (
                result.stdout.strip()
                + "\n"
                + result.stderr.strip()
            )

            prompt = build_validation_prompt(validation_output)

            try:
                ai_response = ask_groq(prompt)
                ai_provider = "Groq"

            except Exception:
                ai_response = ask_ollama(prompt)
                ai_provider = "Ollama"

            results.append({
                "file": file_name,
                "status": "FAIL",
                "output": result.stdout.strip(),
                "error": result.stderr.strip(),
                "ai_provider": ai_provider,
                "ai_explanation": ai_response
            })

    # Overall status
    overall_status = "PASS" if failed == 0 else "FAIL"

    return {
        "overall_status": overall_status,
        "total_files": len(iac_files),
        "passed": passed,
        "failed": failed,
        "results": results
    }