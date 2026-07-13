def generate_signal(data):
    score = 0

    if data["ema20"] > data["ema50"]:
        score += 25

    if data["rsi"] < 30:
        score += 25
    elif data["rsi"] > 70:
        score -= 25

    if data["macd"] > data["macd_signal"]:
        score += 25

    if data["close"] < data["bb_low"]:
        score += 25
    elif data["close"] > data["bb_high"]:
        score -= 25

    if score >= 75:
    return {
        "signal": "STRONG BUY",
        "score": score
    }
elif score >= 50:
    return {
        "signal": "BUY",
        "score": score
    }
elif score <= -50:
    return {
        "signal": "SELL",
        "score": score
    }
else:
    return {
        "signal": "HOLD",
        "score": score
    }
