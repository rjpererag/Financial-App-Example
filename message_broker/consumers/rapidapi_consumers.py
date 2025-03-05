import pika
from src.utils.logger import logger
from src.settings.message_broker import MessageBrokerSettings


def receive_message(settings: MessageBrokerSettings):

    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=settings.connection_params.host))
    channel = connection.channel()
    channel.queue_declare(queue=settings.queue_name)

    def callback(ch, method, properties, body):
        settings.callback_func(body=body)

    channel.basic_consume(queue=settings.queue_name,
                          on_message_callback=callback,
                          auto_ack=True)

    logger.info("Waiting for messages")
    channel.start_consuming()
