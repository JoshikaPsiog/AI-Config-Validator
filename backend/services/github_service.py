import os
import subprocess


def clone_repository(repo_url: str):

    # Project root
    backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    project_root = os.path.dirname(backend_dir)

    # repositories folder
    repo_folder = os.path.join(project_root, "repositories")
    os.makedirs(repo_folder, exist_ok=True)

    # Repository name
    repo_name = repo_url.rstrip("/").split("/")[-1].replace(".git", "")
    destination = os.path.join(repo_folder, repo_name)

    # If repository already exists, use it
    if os.path.exists(destination):
        return {
            "success": True,
            "path": destination
        }

    # Clone repository
    result = subprocess.run(
        ["git", "clone", repo_url, destination],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return {
            "success": False,
            "error": result.stderr
        }

    return {
        "success": True,
        "path": destination
    }