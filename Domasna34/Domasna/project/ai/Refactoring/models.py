from pydantic import BaseModel
from typing import List

class HistoricalDataItem(BaseModel):
    """
    Represents a single historical data point.
    """
    date: str  # Date in 'YYYY-MM-DD' format
    average_price: float  # Average stock price

class HistoricalData(BaseModel):
    """
    Represents a collection of historical data points.
    """
    data: List[HistoricalDataItem]
