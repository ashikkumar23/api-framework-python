import json
from pathlib import Path

BASE_PATH = Path.cwd().joinpath("data")


def read_file(file_name):
    file_path = get_file_with_json_ext(file_name)
    with open(file_path, mode="r", encoding="utf-8") as f:
        return json.load(f)


def get_file_with_json_ext(file_name):
    return (
        BASE_PATH.joinpath(file_name)
        if ".json" in file_name
        else BASE_PATH.joinpath(f"{file_name}.json")
    )
