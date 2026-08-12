import subprocess
import os


def validate_bicep(file_path: str, project_root: str):

    from pathlib import Path

    json_file = str(Path(file_path).with_suffix(".json"))

    # Step 1 - Compile Bicep
    build = subprocess.run(
        [
            "cmd",
            "/c",
            "az",
            "bicep",
            "build",
            "--file",
            file_path
        ],
        capture_output=True,
        text=True,
        cwd=project_root
    )

    if build.returncode != 0:
        return {
            "status": "FAIL",
            "output": build.stderr
        }

    # Step 2 - Validate ARM JSON
    result = subprocess.run(
        [
            "cmd",
            "/c",
            "conftest",
            "test",
            json_file,
            "--policy",
            "policies/bicep"
        ],
        capture_output=True,
        text=True,
        cwd=project_root
    )

    if result.returncode == 0:
        return {
            "status": "PASS",
            "output": result.stdout.strip()
        }

    return {
        "status": "FAIL",
        "output": result.stdout.strip() + "\n" + result.stderr.strip()
    }