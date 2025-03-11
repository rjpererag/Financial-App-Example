from src.message_broker.consumers.rapidapi_consumers import receive_message
from src.message_broker.callbacks.market_value_db import call_back_func
from src.settings import create_settings


if __name__ == "__main__":
    settings = create_settings()
    settings.broker.callback_func = call_back_func
    receive_message(
        broker_settings=settings.broker,
        db_settings=settings.db)
