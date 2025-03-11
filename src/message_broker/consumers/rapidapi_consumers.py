import pika
from src.utils.logger import logger
from src.settings.message_broker import MessageBrokerSettings
from src.settings.db_authentication import DBCredentials
from src.service.market_db_handler import MarketDBHandler


def receive_message(broker_settings: MessageBrokerSettings,
                    db_settings: DBCredentials):

    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=broker_settings.connection_params.host))
    channel = connection.channel()
    channel.queue_declare(queue=broker_settings.queue_name)

    db_handler = MarketDBHandler(creds=db_settings)

    def callback(ch, method, properties, body):
        broker_settings.callback_func(body=body, db_handler=db_handler)

    channel.basic_consume(queue=broker_settings.queue_name,
                          on_message_callback=callback,
                          auto_ack=True)

    logger.info("Waiting for messages")
    channel.start_consuming()
