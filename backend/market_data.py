from binance.client import Client
import pandas as pd

client = Client()


def get_price(symbol="BTCUSDT"):
    ticker = client.get_symbol_ticker(symbol=symbol)

    return {
        "symbol": symbol,
        "price": float(ticker["price"])
    }


def get_klines(symbol="BTCUSDT", interval="5m", limit=100):
    klines = client.get_klines(
        symbol=symbol,
        interval=interval,
        limit=limit
    )

    df = pd.DataFrame(klines)

    df = df.iloc[:, :6]

    df.columns = [
        "time",
        "open",
        "high",
        "low",
        "close",
        "volume"
    ]

    df[["open", "high", "low", "close", "volume"]] = df[
        ["open", "high", "low", "close", "volume"]
    ].astype(float)

    return df
