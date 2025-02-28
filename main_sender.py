from message_broker.producers.rapidapi_producer import send_message


if __name__ == "__main__":
    send_message("Hello, RabbitMQ!")
    send_message("Another message!")
