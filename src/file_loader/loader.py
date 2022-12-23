import ast
from django.core.files.storage import FileSystemStorage
from .validators import (
    validate_pareto_front_file,
    validate_requirements_file,
    validate_stakeholders_file
)
from .constants import (
    pareto_front_file_name,
    requirements_file_name,
    stakeholders_file_name
)

def __save_file(file_name: str, file) -> None:
    """
    Save the provided file with the provided name, 
    replacing the existing file if already exists.
    :file_name str: the desired name for the saved file.
    :file: the file to save
    """
    fs = FileSystemStorage()
    if fs.exists(file_name):
        fs.delete(file_name)
    fs.save(file_name, file)

def upload_files(files: list) -> None:
    """
    Saves the relevant files from a list of provided files.
    """
    for file in files:
        if pareto_front_file_name == file.name:
            validate_pareto_front_file(file)
            __save_file(pareto_front_file_name, file)

        if requirements_file_name == file.name:
            validate_requirements_file(file)
            __save_file(requirements_file_name, file)

        if stakeholders_file_name == file.name:
            validate_stakeholders_file(file)
            __save_file(stakeholders_file_name, file)

    del files

def get_pareto_front() -> dict:
    """
    Returns the pareto-front as a dict
    """
    fs = FileSystemStorage()
    file = fs.open(pareto_front_file_name)
    pf = ast.literal_eval(file.read().decode())

    return pf

def get_requirements() -> dict:
    """
    Returns the requirements as a dict
    """
    fs = FileSystemStorage()
    file = fs.open(requirements_file_name)
    req = ast.literal_eval(file.read().decode())

    return req

def get_stakeholders() -> dict:
    """
    Returns the stakeholders as a dict
    """
    fs = FileSystemStorage()
    file = fs.open(stakeholders_file_name)
    stk = ast.literal_eval(file.read().decode())

    return stk