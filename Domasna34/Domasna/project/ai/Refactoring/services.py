import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from app.models import HistoricalData


def predict_next_month_price(historical_data: HistoricalData) -> float:
    """
    Predicts the average stock price for the next 30 days using ARIMA.

    Args:
        historical_data (HistoricalData): Historical stock price data.

    Returns:
        float: Predicted average price for the next month.

    Raises:
        ValueError: If the input data is insufficient for a prediction.
    """
    # Convert Pydantic model to pandas DataFrame
    data = pd.DataFrame([item.dict() for item in historical_data.data])

    # Set the date as the index and ensure it's in datetime format
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)

    # Check for missing values and drop them
    data = data.dropna()

    if len(data) < 30:
        raise ValueError("Not enough data to make a reliable prediction.")

    # Apply ARIMA model
    model = ARIMA(data['average_price'], order=(5, 1, 0))  # Adjust order if needed
    model_fit = model.fit()

    # Forecast for 30 days (next month)
    forecast = model_fit.forecast(steps=30)

    # Return the mean forecast price for the next month
    return forecast.mean()
