from src.service.finance_api import FinanceAPIConsumer

from src.service.market_db_handler import MarketDBHandler
from src.settings.db_authentication import DBCredentials

from decouple import config

# This is the incoming message
TEST_DATA = {"APPL": {
    "data": {
        "language": "en-US",
        "region": "US",
        "short_name": "Apple Inc.",
        "long_name": "Apple Inc.",
        "market_state": "PRE",
        "exchange": "NMS",
        "market": "us_market",
        "currency": "USD",
        "price_hint": 10,
        "financial_currency": "USD",
        "market_cap": 900000000000,
        "book_value": 13.5,
        "display_name": "Apple",
        "symbol": "APPL"},
    "action": "insert",
    "time": "2025-03-08-58-43"},
    "MSFT": {
        "data": {
            "language": "en-US",
            "region": "US",
            "short_name": "Microsoft Corp.",
            "long_name": "Microsoft Corporation",
            "market_state": "PRE",
            "exchange": "NMS",
            "market": "us_market",
            "currency": "USD",
            "price_hint": 4,
            "financial_currency": "USD",
            "market_cap": 500000000000,
            "book_value": 7.3,
            "display_name": "Microsoft",
            "symbol": "MSFT"},
        "action": "insert",
        "time": "2025-03-08-58-43"}}


if __name__ == "__main__":
    db_settings = DBCredentials(
        db_user=config("DB_USER"),
        db_password=config("DB_PASSWORD"),
        db_name=config("DB_NAME"),
        db_port=config("DB_PORT"),
    )

    handler = MarketDBHandler(creds=db_settings)
    handler.process_message(msg=TEST_DATA)
