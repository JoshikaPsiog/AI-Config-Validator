import os
import sys
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import services.file_service as file_service
def test_get_file_path():
    path = file_service.get_file_path("sample.tf")
    assert "sample.tf" in path


def test_file_exists_true():
    with tempfile.TemporaryDirectory() as temp:
        file_service.UPLOAD_FOLDER = temp

        file_path = os.path.join(temp, "sample.tf")
        with open(file_path, "w") as f:
            f.write("test")

        assert file_service.file_exists("sample.tf") is True


def test_file_exists_false():
    with tempfile.TemporaryDirectory() as temp:
        file_service.UPLOAD_FOLDER = temp

        assert file_service.file_exists("missing.tf") is False


def test_read_file():
    with tempfile.TemporaryDirectory() as temp:
        file_service.UPLOAD_FOLDER = temp

        file_path = os.path.join(temp, "sample.tf")

        with open(file_path, "w") as f:
            f.write("terraform")

        assert file_service.read_file("sample.tf") == "terraform"


def test_get_terraform_files():
    with tempfile.TemporaryDirectory() as temp:
        file_service.UPLOAD_FOLDER = temp

        open(os.path.join(temp, "a.tf"), "w").close()
        open(os.path.join(temp, "b.tf"), "w").close()
        open(os.path.join(temp, "c.txt"), "w").close()

        files = file_service.get_terraform_files()

        assert "a.tf" in files
        assert "b.tf" in files
        assert "c.txt" not in files


def test_get_terraform_files_empty():
    with tempfile.TemporaryDirectory() as temp:
        file_service.UPLOAD_FOLDER = temp

        files = file_service.get_terraform_files()

        assert files == []