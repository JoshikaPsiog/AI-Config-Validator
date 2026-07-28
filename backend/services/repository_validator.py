import os
import subprocess
import re
from ai.ollama_service import ask_ollama
from ai.prompt_builder import build_security_prompt

def validate_repository(terraform_files):

    results = []

    backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    project_root = os.path.dirname(backend_dir)

    for tf_file in terraform_files:

        if tf_file.endswith(".tf"):
            policy_path = os.path.join(project_root, "policies", "terraform")

        elif tf_file.endswith(".bicep"):
            policy_path = os.path.join(project_root, "policies", "bicep")

        relative_file = os.path.basename(tf_file)

        result = subprocess.run(
            [
                "conftest",
                "test",
                tf_file,      
                "-p",
                policy_path
            ],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:

            results.append(
                {
                    "file": relative_file,
                    "status": "PASS"
                }
            )

        else:

            reason = result.stdout + result.stderr
            reason = re.sub(r'\x1b\[[0-9;]*m', '', reason)
            reason = reason.replace(tf_file, relative_file)

            prompt = build_security_prompt(reason)
            ai_response = ask_ollama(prompt)

            results.append(
                {
                    "file": relative_file,
                    "status": "FAIL",
                    "reason": reason,
                    "ai_explanation": ai_response
                }
            )

    return results