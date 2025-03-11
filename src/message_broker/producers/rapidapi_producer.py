import pika
from ...utils.logger import logger
from ...settings.message_broker import MessageBrokerSettings


def send_message(settings: MessageBrokerSettings,  message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=settings.connection_params.host))
    channel = connection.channel()

    channel.queue_declare(queue=settings.queue_name)
    channel.basic_publish(exchange='',
                          routing_key=settings.queue_name,
                          body=message)

    logger.info(f"Sent: {message}")
    connection.close()
