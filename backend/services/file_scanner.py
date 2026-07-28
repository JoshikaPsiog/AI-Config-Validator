import os


def find_terraform_files(folder_path):

    terraform_files = []

    for root, dirs, files in os.walk(folder_path):

        for file in files:

           if file.endswith(".tf") or file.endswith(".bicep"):

                terraform_files.append(
                    os.path.join(root, file)
                )

    return terraform_files