from ..requests.requestor import EndpointRequestor
from ..dataclasses import *


class YahooFinanceAPI:

    def __init__(self, headers: dict):
        self.headers = headers
        self.requestor = EndpointRequestor()

    def get_stock_quotes(self, ticker: str) -> StockQuotes:
        url = "https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/quotes"
        params = {
            "ticker": ticker
        }

        response = self.requestor.get(
            url=url, headers=self.headers, params=params
        )

        status = response.get("meta", {}).get("status")
        if status == 200:
            return StockQuotes(
                status=status,
                response=[QuoteBodyModel(**item) for item in response.get("body", [])]
            )

