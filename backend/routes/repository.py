from fastapi import APIRouter
from pydantic import BaseModel

from services.github_service import clone_repository
from services.file_scanner import find_terraform_files
from services.repository_validator import validate_repository

router = APIRouter()


class RepositoryRequest(BaseModel):
    repo_url: str


@router.post("/scan-repository")
def scan_repository(request: RepositoryRequest):

    clone_result = clone_repository(request.repo_url)

    if not clone_result["success"]:
        return clone_result

    repo_path = clone_result["path"]

    terraform_files = find_terraform_files(repo_path)

    try:

        validation_results = validate_repository(terraform_files)

        passed = sum(1 for r in validation_results if r["status"] == "PASS")
        failed = sum(1 for r in validation_results if r["status"] == "FAIL")

        return {
            "repository": request.repo_url,
            "repository_path": repo_path,
            "terraform_files_found": len(terraform_files),
            "passed": passed,
            "failed": failed,
            "results": validation_results
        }

    except Exception as e:

        return {
            "status": "ERROR",
            "message": str(e)
        }