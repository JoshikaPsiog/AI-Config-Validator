import os


def read_terraform_files(terraform_files):

    files_data = []

    for file_path in terraform_files:

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            files_data.append({
                "file_name": os.path.basename(file_path),
                "file_path": file_path,
                "content": content
            })

        except Exception as e:
            files_data.append({
                "file_name": os.path.basename(file_path),
                "file_path": file_path,
                "error": str(e)
            })

    return files_data