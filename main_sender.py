from src.service.finance_api import FinanceAPIConsumer
from src.settings.message_broker import MessageBrokerSettings


if __name__ == "__main__":
    settings = MessageBrokerSettings()
    api_consumer = FinanceAPIConsumer(mssg_broker_settings=settings)
    api_consumer.continuous_consume(ticker="AAPL", with_wait_time=True, max_items=3, timer=2)
