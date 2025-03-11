from message_broker.consumers.rapidapi_consumers import receive_message
from src.settings.message_broker import MessageBrokerSettings
from src.service.market_db_handler import DBHandler
from src.settings.db_authentication import DBCredentials

from src.utils.logger import logger

from decouple import config
import json


def decode_message(body: bytes) -> dict | None:  # TODO: Move to utils

    try:
        mssg = body.decode("utf-8")
        return json.loads(mssg)
    except Exception as e:
        logger.error(f"Error decoding message: {str(body)}. {str(e)}")


def call_back_func(body):
    if message := decode_message(body=body):
        logger.info(f"Loading data into db")
        return message


if __name__ == "__main__":
    settings = MessageBrokerSettings()
    db_settings = DBCredentials(
        db_user=config("DB_USER"),
        db_password=config("DB_PASSWORD"),
        db_name=config("DB_NAME"),
        db_port=config("DB_PORT"),
    )

    settings.callback_func = call_back_func
    receive_message(settings=settings, db_settings=db_settings)
