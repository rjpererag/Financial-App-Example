from src.service.finance_api import FinanceAPIConsumer
from src.settings.message_broker import MessageBrokerSettings


if __name__ == "__main__":
    settings = MessageBrokerSettings()
    path = "test_data/fake_rapidapi_data/data.pkl"
    api_consumer = FinanceAPIConsumer(mssg_broker_settings=settings)
    api_consumer.local_api_consumption(data_path=path)
