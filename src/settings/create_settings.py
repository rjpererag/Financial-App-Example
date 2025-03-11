from ..settings.db_authentication import DBCredentials
from ..settings.message_broker import MessageBrokerSettings

from dataclasses import dataclass, field
from decouple import config


@dataclass
class Settings:
    broker: MessageBrokerSettings = field(default_factory=MessageBrokerSettings)
    db: DBCredentials = field(default_factory=DBCredentials)


def create_settings() -> Settings:
    return Settings(
        broker=MessageBrokerSettings(),
        db=DBCredentials(
            db_user=config("DB_USER"),
            db_password=config("DB_PASSWORD"),
            db_name=config("DB_NAME"),
            db_port=config("DB_PORT")
        ))
