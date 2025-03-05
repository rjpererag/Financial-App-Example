import json
import pickle
from typing import Any


class FileManager:

    @staticmethod
    def save_pickle(path: str, object_: Any):
        with open(path, "wb") as file:
            pickle.dump(object_, file)

    @staticmethod
    def save_json(path: str, object_) -> None:
        with open(path, "w") as json_file:
            json.dump(object_, json_file, indent=2)

    @staticmethod
    def load_json(path: str):
        with open(path, "r") as json_file:
            return json.load(json_file)

    @staticmethod
    def read_pickle(path: str):
        with open(path, "rb") as file:
            return pickle.load(file)
