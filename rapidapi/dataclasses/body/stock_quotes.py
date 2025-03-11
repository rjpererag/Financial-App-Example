from pydantic import BaseModel, Field
from typing import Optional, List


class QuoteBodyModel(BaseModel):
    language: str = Field(None, alias="language")
    region: str = Field(None, alias="region")
    short_name: str = Field(None, alias="shortName")
    long_name: str = Field(None, alias="longName")
    market_state: str = Field(None, alias="marketState")
    exchange: str = Field(None, alias="exchange")
    market: str = Field(None, alias="market")
    currency: str = Field(None, alias="currency")
    price_hint: int = Field(None, alias="priceHint")
    financial_currency: str = Field(None, alias="financialCurrency")
    market_cap: int = Field(None, alias="marketCap")
    book_value: Optional[float] = Field(None, alias="bookValue")
    display_name: Optional[str] = Field(None, alias="displayName")
    symbol: str = Field(None, alias="symbol")
