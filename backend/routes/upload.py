from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import shutil

router = APIRouter()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Supported IaC file types
ALLOWED_EXTENSIONS = [".tf", ".bicep"]


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    extension = os.path.splitext(file.filename)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only .tf and .bicep files are supported."
        )

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "status": "success",
        "filename": file.filename,
        "file_type": extension,
        "path": filepath
    }