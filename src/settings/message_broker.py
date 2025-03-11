from dataclasses import dataclass, field
from typing import Callable


@dataclass
class ConnectionParams:
    host: str = "localhost"


def default_callback_func(body, **kwargs) -> None:
    print(body)
    print("--------------------------------------------------------------------")


@dataclass
class MessageBrokerSettings:
    connection_params: ConnectionParams = field(default_factory=ConnectionParams)
    queue_name: str = "my_queue"
    callback_func: Callable = default_callback_func
