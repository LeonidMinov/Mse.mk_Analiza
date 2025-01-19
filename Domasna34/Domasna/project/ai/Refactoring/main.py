from fastapi import FastAPI, HTTPException
from app.models import HistoricalData
from app.services import predict_next_month_price

app = FastAPI()


@app.post("/predict-next-month-price/")
async def predict_next_month_price_endpoint(historical_data: HistoricalData):
    """
    Endpoint to predict the average stock price for the next month.

    Args:
        historical_data (HistoricalData): Historical stock price data.

    Returns:
        dict: Predicted average price for the next month.
    """
    try:
        predicted_price = predict_next_month_price(historical_data)
        return {"predicted_next_month_price": predicted_price}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
