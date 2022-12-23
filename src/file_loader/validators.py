import ast
from .constants import (
    pareto_front_file_name,
    requirements_file_name,
    stakeholders_file_name
)

def validate_pareto_front_file(file):
    data = ast.literal_eval(file.read().decode())

    if not set(['id','profit','cost','reqs','stks']).issubset(set(data['0'].keys())):
        raise Exception(f"The file '{pareto_front_file_name}' does not meet the standard "+
                        "(it must have 'id', 'profit', 'cost', 'reqs' and 'stks' fields)")

    if (len(data) < 3):
        raise Exception(f"The file '{pareto_front_file_name}' must have at least 3 elements")

def validate_requirements_file(file):
    req = ast.literal_eval(file.read().decode())

    if not (set(["id", "keys"]).issubset(set(req['0'].keys()))):
        raise Exception(f"The file '{requirements_file_name}' does not meet the standard "+
                        "(it must have 'id' and 'keys' fields)")

def validate_stakeholders_file(file):
    stk = ast.literal_eval(file.read().decode())

    if not (set(["id", "keys"]).issubset(set(stk['0'].keys()))):
        raise Exception(f"The file '{stakeholders_file_name}' does not meet the standard "+
                        "(it must have 'id' and 'keys' fields)")