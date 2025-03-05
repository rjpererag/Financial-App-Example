import json


def save_json(path: str, object_) -> None:
    with open(path, "w") as json_file:
        json.dump(object_, json_file, indent=2)


def load_json(path: str):
    with open(path, "r") as json_file:
        return json.load(json_file)
