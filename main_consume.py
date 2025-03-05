from message_broker.consumers.rapidapi_consumers import receive_message
from src.settings.message_broker import MessageBrokerSettings


if __name__ == "__main__":
    settings = MessageBrokerSettings()
    receive_message(settings=settings)
