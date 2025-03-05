from dataclasses import dataclass, field
from .body import QuoteBodyModel


@dataclass
class StockQuotes:
    status: int
    response: list[QuoteBodyModel] = field(default_factory=list)
