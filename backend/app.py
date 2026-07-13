from fastapi import FastAPI

from market_data import get_price
from analysis import analyze_market

app = FastAPI(
    title="Crypto AI Signal Pro"
)

@app.get("/")
def home():
    return {
        "message": "Crypto AI Signal Pro API"
    }

@app.get("/price")
def price():
    return get_price()

@app.get("/analysis")
def analysis():
    return analyze_market()
