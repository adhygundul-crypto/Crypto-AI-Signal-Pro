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

    df = pd.DataFrame(klines, columns=[
        "open_time", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "number_of_trades",
        "taker_buy_base", "taker_buy_quote", "ignore"
    ])

    df["open"] = df["open"].astype(float)
    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)
    df["close"] = df["close"].astype(float)
    df["volume"] = df["volume"].astype(float)

    return df
