from decouple import config
from .endpoints import YahooFinanceAPI


class RapidAPI:
	yahoo_finance = YahooFinanceAPI(headers={
		"x-rapidapi-key": config("RAPIDAPI_KEY"),
		"x-rapidapi-host": "yahoo-finance15.p.rapidapi.com"
	})
