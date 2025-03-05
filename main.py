from src.service.finance_api import FinanceAPIConsumer


def main() -> None:
    path = "test_data/fake_rapidapi_data/data.pkl"
    api_consumer = FinanceAPIConsumer()
    api_consumer.local_api_consumption(data_path=path)


if __name__ == "__main__":
    main()
