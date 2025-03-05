from rapidapi.dataclasses.stock_quotes import StockQuotes, QuoteBodyModel
import json
import pickle
import random


fake_base_data = {
    1: {
        "shortName": "Apple Inc.",
        "longName": "Apple Inc.",
        "priceHint": 2,
        "marketCap": 300000000000,
        "bookValue": 4.5,
        "displayName": "Apple",
        "symbol": "APPL"
    },
    2: {
        "shortName": "Microsoft Corp.",
        "longName": "Apple Corporation",
        "priceHint": 4,
        "marketCap": 500000000000,
        "bookValue": 7.3,
        "displayName": "Microsoft",
        "symbol": "MSFT"
    },
}


def modify_fake_data(data: dict) -> dict:

    random_multiplier = random.randint(a=1, b=3)

    for key in ["priceHint", "marketCap", "bookValue"]:
        if isinstance(data[key], int | float):
            data[key] = data[key] * random_multiplier

    return data


def create_fake_api_response() -> StockQuotes:

    body = []
    for i in range(2):
        fake_data = fake_base_data[i+1]
        fake_data = modify_fake_data(data=fake_data)

        body.append(QuoteBodyModel(
            language="en-US",
            region="US",
            marketState="PRE",
            exchange="NMS",
            market="us_market",
            currency="USD",
            financialCurrency="USD",
            **fake_data
        ))

    return StockQuotes(
        status=200,
        response=body
    )


def generate_fake_data(size: int) -> list[StockQuotes]:

    fake_responses = []
    for i in range(size):
        fake_responses.append(create_fake_api_response())
    return fake_responses


def save_fake_data(path: str, object_: list[StockQuotes]) -> None:

    data_to_save_json = [{
        "status": item.status,
        "response": [el.model_dump() for el in item.response]
    } for item in object_]

    json_path = f"{path}.json"
    pickle_path = f"{path}.pkl"

    with open(json_path, "w") as json_file:
        json.dump(data_to_save_json, json_file, indent=2)

    with open(pickle_path, "wb") as file:
        pickle.dump(object_, file)


if __name__ == "__main__":
    fake_data_ = generate_fake_data(size=200)
    save_fake_data(path="test_data/fake_rapidapi_data/data", object_=fake_data_)

