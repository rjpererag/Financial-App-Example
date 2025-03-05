from dataclasses import dataclass
from typing import Callable


@dataclass
class ConnectionParams:
    host: str = "localhost"


def default_callback_func(body) -> None:
    print(body)


@dataclass
class MessageBrokerSettings:
    connection_params: ConnectionParams = ConnectionParams()
    queue_name: str = "my_queue"
    callback_func: Callable = default_callback_func
