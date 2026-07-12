from binance.client import Client

client = Client()


def get_price(symbol="BTCUSDT"):
    ticker = client.get_symbol_ticker(symbol=symbol)

    return {
        "symbol": symbol,
        "price": float(ticker["price"])
    }


if __name__ == "__main__":
    data = get_price()
    print(data)
