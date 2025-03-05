from pydantic import BaseModel, Field
from typing import Optional, List


class QuoteBodyModel(BaseModel):
    # pre_market_change: Optional[float] = Field(None, alias="preMarketChange")
    # pre_market_change_percent: Optional[float] = Field(None, alias="preMarketChangePercent")
    # pre_market_price: Optional[float] = Field(None, alias="preMarketPrice")
    # pre_market_time: Optional[int] = Field(None, alias="preMarketTime")
    # post_market_change: Optional[float] = Field(None, alias="postMarketChange")
    # post_market_change_percent: Optional[float] = Field(None, alias="postMarketChangePercent")
    # post_market_price: Optional[float] = Field(None, alias="postMarketPrice")
    # post_market_time: Optional[int] = Field(None, alias="postMarketTime")
    language: str = Field(None, alias="language")
    region: str = Field(None, alias="region")
    # quote_type: str = Field(None, alias="quoteType")
    # type_disp: Field(None, alias="typeDisp")
    # quote_source_name: Optional[str] = Field(None, alias="quoteSourceName")
    # triggerable: bool = Field(None, alias="triggerable")
    # custom_price_alert_confidence: Optional[str] = Field(None, alias="customPriceAlertConfidence")
    # regular_market_change_percent: Optional[str] = Field(None, alias="regularMarketChangePercent")
    # regular_market_price: float = Field(None, alias="regularMarketPrice")
    short_name: str = Field(None, alias="shortName")
    long_name: str = Field(None, alias="longName")
    market_state: str = Field(None, alias="marketState")
    exchange: str = Field(None, alias="exchange")
    # message_board_id: Optional[str] = Field(None, alias="messageBoardId")
    # exchange_timezone_name: Optional[str] = Field(None, alias="exchangeTimezoneName")
    # exchange_timezone_short_name: Optional[str] = Field(None, alias="exchangeTimezoneShortName")
    # gmt_offset_milliseconds: Optional[int | float] = Field(None, alias="gmtOffSetMilliseconds")
    market: str = Field(None, alias="market")
    # esg_populated: bool = Field(None, alias="esgPopulated")
    # corporate_actions: List = Field(list, alias="corporateActions")
    # regular_market_time: int = Field(None, alias="regularMarketTime")
    currency: str = Field(None, alias="currency")
    # has_pre_post_market_data: bool = Field(None, alias="firstTradeDateMilliseconds")
    # first_trade_date_milliseconds: Optional[int] = Field(None, alias="firstTradeDateMilliseconds")
    price_hint: int = Field(None, alias="priceHint")
    # regular_market_change: float = Field(None, alias="regularMarketChange")
    # regular_market_day_high: float = Field(None, alias="regularMarketDayHigh")
    # regular_market_day_range: str = Field(None, alias="regularMarketDayRange")
    # regular_market_day_low: float = Field(None, alias="regularMarketDayLow")
    # regular_market_volume: int = Field(None, alias="regularMarketVolume")
    # regular_market_previous_close: float = Field(None, alias="regularMarketPreviousClose")
    # bid: float = Field(None, alias="bid")
    # ask: float = Field(None, alias="ask")
    # bid_size: int = Field(None, alias="bidSize")
    # ask_size: int = Field(None, alias="askSize")
    # full_exchange_name: str = Field(None, alias="fullExchangeName")
    financial_currency: str = Field(None, alias="financialCurrency")
    # regular_market_open: float = Field(None, alias="regularMarketOpen")
    # average_daily_volume_3_month: int = Field(None, alias="averageDailyVolume3Month")
    # average_daily_volume_10_day: int = Field(None, alias="averageDailyVolume10Day")
    # two_hundred_day_average_change: float = Field(None, alias="twoHundredDayAverageChange")
    # two_hundred_day_average_change_percent: float = Field(None, alias="twoHundredDayAverageChangePercent")
    market_cap: int = Field(None, alias="marketCap")
    # forward_pe: Optional[float] = Field(None, alias="forwardPE")
    # price_to_book: Optional[float] = Field(None, alias="priceToBook")
    # source_interval: int = Field(None, alias="sourceInterval")
    # exchange_data_delayed_by: int = Field(None, alias="exchangeDataDelayedBy")
    # average_analyst_rating: Optional[str] = Field(None, alias="averageAnalystRating")
    # tradeable: bool = Field(None, alias="tradeable")
    # crypto_tradeable: bool = Field(None, alias="cryptoTradeable")
    # fifty_two_week_low_change: float = Field(None, alias="fiftyTwoWeekLowChange")
    # fifty_two_week_low_change_percent: float = Field(None, alias="fiftyTwoWeekLowChangePercent")
    # fifty_two_week_range: str = Field(None, alias="fiftyTwoWeekRange")
    # fifty_two_week_high_change: float = Field(None, alias="fiftyTwoWeekHighChange")
    # fifty_two_week_high_change_percent: float = Field(None, alias="fiftyTwoWeekHighChangePercent")
    # fifty_two_week_low: float = Field(None, alias="fiftyTwoWeekLow")
    # fifty_two_week_high: float = Field(None, alias="fiftyTwoWeekHigh")
    # fifty_two_week_change_percent: float = Field(None, alias="fiftyTwoWeekChangePercent")
    # dividend_date: Optional[int] = Field(None, alias="dividendDate")
    # earnings_timestamp: Optional[int] = Field(None, alias="earningsTimestamp")
    # earnings_timestamp_start: Optional[int] = Field(None, alias="earningsTimestampStart")
    # earnings_timestamp_end: Optional[int] = Field(None, alias="earningsTimestampEnd")
    # earnings_call_timestamp_start: Optional[int] = Field(None, alias="earningsCallTimestampStart")
    # earnings_call_timestamp_end: Optional[int] = Field(None, alias="earningsCallTimestampEnd")
    # is_earnings_date_estimate: bool = Field(None, alias="isEarningsDateEstimate")
    # trailing_annual_dividend_rate: Optional[float] = Field(None, alias="trailingAnnualDividendRate")
    # trailing_pe: Optional[float] = Field(None, alias="trailingPE")
    # dividend_rate: Optional[float] = Field(None, alias="dividendRate")
    # trailing_annual_dividend_yield: Optional[float] = Field(None, alias="trailingAnnualDividendYield")
    # dividend_yield: Optional[float] = Field(None, alias="dividendYield")
    # eps_trailing_twelve_months: float = Field(None, alias="epsTrailingTwelveMonths")
    # eps_forward: Optional[float] = Field(None, alias="epsForward")
    # eps_current_year: Optional[float] = Field(None, alias="epsCurrentYear")
    # price_eps_current_year: Optional[float] = Field(None, alias="priceEpsCurrentYear")
    # shares_outstanding: int = Field(None, alias="sharesOutstanding")
    book_value: Optional[float] = Field(None, alias="bookValue")
    # fifty_day_average: float = Field(None, alias="fiftyDayAverage")
    # fifty_day_average_change: float = Field(None, alias="fiftyDayAverageChange")
    # fifty_day_average_change_percent: float = Field(None, alias="fiftyDayAverageChangePercent")
    # two_hundred_day_average: float = Field(None, alias="twoHundredDayAverage")
    display_name: Optional[str] = Field(None, alias="displayName")
    symbol: str = Field(None, alias="symbol")
