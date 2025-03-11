import json
from .logger import logger


def save_json(path: str, object_) -> None:
    with open(path, "w") as json_file:
        json.dump(object_, json_file, indent=2)


def load_json(path: str):
    with open(path, "r") as json_file:
        return json.load(json_file)


def decode_message(body: bytes) -> dict | None:

    try:
        mssg = body.decode("utf-8")
        return json.loads(mssg)
    except Exception as e:
        logger.error(f"Error decoding message: {str(body)}. {str(e)}")
