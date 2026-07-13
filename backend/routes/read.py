from fastapi import APIRouter

from services.file_service import file_exists, read_file

router = APIRouter()


@router.get("/read/{filename}")
def read(filename: str):

    if not file_exists(filename):
        return {
            "error": "File not found"
        }

    content = read_file(filename)

    return {
        "filename": filename,
        "content": content
    }

from services.file_service import get_terraform_files


@router.get("/terraform-files")
def terraform_files():

    return {
        "terraform_files": get_terraform_files()
    }