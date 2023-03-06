import requests
import os
from dotenv import load_dotenv
from alpaca.trading.client import TradingClient
from alpaca.data.live.crypto import CryptoDataStream
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce


def createDayOrder():
    print("Creating order...")
    ticker = "AAPL"
    qty = 1
    side = "buy"
    orderType = "market"

    data = {
        "symbol": ticker,
        "qty": qty,
        "side": side,
        "type": orderType,
        "time_in_force": "day"
    }

    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)

    return r.content


async def bar_callback(bar):
    for property_name, value in bar:
        print(f"\"{property_name}\": {value}")

if __name__ == "__main__":
    print("Starting the program...")
    # TODO: Take in live market data
    # TODO: Create a trading strategy
    load_dotenv()
    ALPACA_KEY = os.environ.get('ALPACA_KEY')
    ALPACA_SECRET_KEY = os.environ.get('ALPACA_SECRET_KEY')
    BASE_URL = os.environ.get('ALPACA_BASE_URL')

    # tradingClient = TradingClient(ALPACA_KEY, ALPACA_SECRET_KEY, paper=True)
    # account = tradingClient.get_account()

    # if ALPACA_KEY is not None and ALPACA_SECRET_KEY is not None:
    #     crypto_stream = CryptoDataStream(ALPACA_KEY, ALPACA_SECRET_KEY)

    #     # Subscribing to bar event
    #     symbol = "BTC/USD"
    #     crypto_stream.subscribe_bars(bar_callback, symbol)

    #     crypto_stream.run()

    HEADERS: dict = {'APCA-API-KEY-ID': ALPACA_KEY,
                     'APCA-API-SECRET-KEY': ALPACA_SECRET_KEY}
    ORDERS_URL = f'{BASE_URL}/v2/orders'
