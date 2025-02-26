from rapidapi import RapidAPI
from src.utils.utils import *


def main() -> None:

    api = RapidAPI().yahoo_finance
    ticker = "AAPL,MSFT"
    response = api.get_stock_quotes(ticker=ticker)

    data_to_save = [item.model_dump() for item in response.response]

    saving_path = "test_data/get_stock_quotes_response_2.json"
    save_json(path=saving_path, object_=data_to_save)

    print(response)


if __name__ == "__main__":
    main()
