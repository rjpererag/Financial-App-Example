from ..requests.requestor import EndpointRequestor


class YahooFinanceAPI:

    def __init__(self, headers: dict):
        self.headers = headers
        self.requestor = EndpointRequestor()

    def get_stock_quotes(self, ticker: str):
        url = "https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/quotes"
        params = {
            "ticker": ticker
        }
        return self.requestor.get(
            url=url, headers=self.headers, params=params
        )
