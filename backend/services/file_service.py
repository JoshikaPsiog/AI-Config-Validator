import os

UPLOAD_FOLDER = "../uploads"


def get_file_path(filename):
    return os.path.join(UPLOAD_FOLDER, filename)


def file_exists(filename):
    return os.path.exists(get_file_path(filename))


def read_file(filename):

    file_path = get_file_path(filename)

    with open(file_path, "r") as file:
        return file.read()
def get_terraform_files():

    terraform_files = []

    for file in os.listdir(UPLOAD_FOLDER):

        if file.endswith(".tf"):
            terraform_files.append(file)

    return terraform_files       