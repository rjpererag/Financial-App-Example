from src.utils import decode_message, logger
from src.service.market_db_handler import MarketDBHandler


def call_back_func(body, **kwargs) -> None:  # Todo: here we will
    db_handler = kwargs.get("db_handler")
    if (message := decode_message(body=body)) and (
            isinstance(db_handler, MarketDBHandler)):

        logger.info(f"Processing message")
        db_handler.process_message(msg=message)
