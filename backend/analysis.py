from market_data import get_klines
from indicators import calculate_indicators
from signal_engine import generate_signal


def analyze_market(symbol="BTCUSDT", timeframe="5m"):
    df = get_klines(symbol=symbol, interval=timeframe)

    df = calculate_indicators(df)

    latest = df.iloc[-1]

    signal = generate_signal(latest)

    return {
        "symbol": symbol,
        "timeframe": timeframe,
        "price": float(latest["close"]),
        "signal": signal,
        "ema20": round(float(latest["ema20"]), 2),
        "ema50": round(float(latest["ema50"]), 2),
        "rsi": round(float(latest["rsi"]), 2),
        "macd": round(float(latest["macd"]), 2),
        "macd_signal": round(float(latest["macd_signal"]), 2),
    }
