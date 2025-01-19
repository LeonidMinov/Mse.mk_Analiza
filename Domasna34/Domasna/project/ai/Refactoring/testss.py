import pytest
from app.models import HistoricalData, HistoricalDataItem
from app.services import predict_next_month_price


def test_predict_next_month_price():
    """
    Tests the predict_next_month_price function.
    """
    historical_data = HistoricalData(data=[
        HistoricalDataItem(date="2024-12-01", average_price=100.5),
        HistoricalDataItem(date="2024-12-02", average_price=101.0),
        HistoricalDataItem(date="2024-12-03", average_price=102.0),
        # Add 30+ data points for realistic tests
    ])

    result = predict_next_month_price(historical_data)

    # Assert that the predicted price is a valid number
    assert isinstance(result, float)
    assert result > 0
