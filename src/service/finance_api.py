import json
from datetime import datetime

from rapidapi.rapidapi import RapidAPI
from rapidapi.dataclasses.stock_quotes import StockQuotes
from rapidapi.dataclasses.body.stock_quotes import QuoteBodyModel

from ..utils.file_manager import FileManager
from ..utils.logger import logger
from ..message_broker.producers.rapidapi_producer import send_message
from ..settings.message_broker import MessageBrokerSettings

from time import sleep


class FinanceAPIConsumer:

    def __init__(self, mssg_broker_settings: MessageBrokerSettings):
        self.api = RapidAPI()
        self.file_manager = FileManager
        self.mssg_broker_settings = mssg_broker_settings

    @staticmethod
    def _format_response(response: QuoteBodyModel, action: str) -> dict:
        now = datetime.now()
        now_str = now.strftime(f"%Y-%m-%H-%M-%S")
        return {"data": {**response.model_dump()}, "action": action, "time": now_str}

    def _create_message(self, response: list[QuoteBodyModel]) -> bytes:
        msg = {resp.symbol: self._format_response(response=resp, action="insert")
               for resp in response if resp is not None} if isinstance(response, list) else None

        if isinstance(msg, dict):
            return json.dumps(msg).encode("utf-8")

    def _send_message(self, call: StockQuotes):
        logger.info("Sending message")
        msg = self._create_message(response=call.response)
        send_message(
            settings=self.mssg_broker_settings,
            message=msg)

    def local_api_consumption(self, data_path: str) -> None:

        api_data = self._load_local_data(path=data_path)
        for _, call in enumerate(api_data):
            try:
                if call and (call.status == 200):
                    self._send_message(call=call)
                sleep(5)

            except Exception as e:
                logger.error(f"Error occurred: {str(e)}. Data: {call}")

    def single_consume(self, ticker: str):
        logger.info(f"Getting market data from: {ticker}")
        call = self.api.yahoo_finance.get_stock_quotes(ticker=ticker)
        if call and (call.status == 200):
            self._send_message(call=call)

    def continuous_consume(self,
                           ticker: str,
                           with_wait_time: bool = False,
                           max_items: int = 0,
                           **kwargs):

        count = 0
        timer = self.__create_timer(with_wait_time=with_wait_time, timer=kwargs.get("timer"))
        while True:

            logger.info(f"Iteration: {count+1}")
            self.single_consume(ticker=ticker)
            count += 1
            if count == max_items:
                break

            sleep(timer)

    @staticmethod
    def __create_timer(with_wait_time: bool, timer: int) -> int:
        if with_wait_time:
            if timer and isinstance(timer, int):
                return timer
            else:
                return 5
        else:
            return 1

    def _load_local_data(self, path: str) -> list[StockQuotes]:
        try:
            return self.file_manager.read_pickle(path=path)
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
