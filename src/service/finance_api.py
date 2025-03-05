import json
from datetime import datetime
from src.utils.file_manager import FileManager
from src.utils.logger import logger
from message_broker.producers.rapidapi_producer import send_message
from src.settings.message_broker import MessageBrokerSettings
from rapidapi.dataclasses.stock_quotes import StockQuotes
from rapidapi.dataclasses.body.stock_quotes import QuoteBodyModel

from time import sleep


class FinanceAPIConsumer:

    def __init__(self, mssg_broker_settings: MessageBrokerSettings):
        self.file_manager = FileManager
        self.mssg_broker_settings = mssg_broker_settings

    @staticmethod
    def _format_response(response: QuoteBodyModel, action: str) -> dict:
        now = datetime.now()
        now_str = now.strftime(f"%Y-%m-%H-%M-%S")
        return {"data": {**response.model_dump()}, "action": action, "time": now_str}

    def _create_message(self, response: list[QuoteBodyModel]) -> str | None:
        msg = {resp.symbol: self._format_response(response=resp, action="insert")
               for resp in response if resp is not None} if isinstance(response, list) else None

        if isinstance(msg, dict):
            return json.dumps(msg).encode("utf-8")

    def local_api_consumption(self, data_path: str) -> None:

        api_data = self._load_local_data(path=data_path)
        for _, call in enumerate(api_data):
            try:
                if call and (call.status == 200):
                    msg = self._create_message(response=call.response)
                    send_message(
                        settings=self.mssg_broker_settings,
                        message=msg)
                sleep(5)  # TODO: Delete

            except Exception as e:
                logger.error(f"Error occurred: {str(e)}. Data: {call}")


    def consume_api(self):
        # TODO
        ...

    def _load_local_data(self, path: str) -> list[StockQuotes]:
        try:
            return self.file_manager.read_pickle(path=path)
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
