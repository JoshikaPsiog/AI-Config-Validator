import os
import subprocess
import re

from ai.groq_service import ask_groq
from ai.ollama_service import ask_ollama
from ai.prompt_builder import build_security_prompt


def validate_repository(terraform_files):

    results = []

    backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    project_root = os.path.dirname(backend_dir)

    for tf_file in terraform_files:

        if tf_file.endswith(".tf"):
            policy_path = os.path.join(
                project_root,
                "policies",
                "terraform"
            )
            file_type = "Terraform"

        elif tf_file.endswith(".bicep"):
            policy_path = os.path.join(
                project_root,
                "policies",
                "bicep"
            )
            file_type = "Bicep"

        else:
            continue

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

        # -----------------------------
        # PASS
        # -----------------------------

        if result.returncode == 0:

            results.append(
                {
                    "file": relative_file,
                    "type": file_type,
                    "status": "PASS",
                    "output": "Validation passed successfully.",
                    "error": ""
                }
            )

        # -----------------------------
        # FAIL
        # -----------------------------

        else:

            reason = result.stdout + result.stderr

            # Remove ANSI escape codes
            reason = re.sub(
                r'\x1b\[[0-9;]*m',
                '',
                reason
            )

            # Replace full path with filename
            reason = reason.replace(
                tf_file,
                relative_file
            )

            prompt = build_security_prompt(reason)

            # -----------------------------
            # Groq → Ollama fallback
            # -----------------------------

            ai_provider = "Groq"

            try:

                ai_response = ask_groq(prompt)

            except Exception as groq_error:

                print(
                    f"Groq failed for {relative_file}: "
                    f"{groq_error}"
                )

                ai_provider = "Ollama"

                ai_response = ask_ollama(prompt)

            results.append(
                {
                    "file": relative_file,
                    "type": file_type,
                    "status": "FAIL",
                    "output": reason,
                    "error": "",
                    "ai_provider": ai_provider,
                    "ai_explanation": ai_response
                }
            )

    return results