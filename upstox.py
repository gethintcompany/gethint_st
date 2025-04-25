import upstox_client
import json
import datetime

def get_instrument_key_from_stock_name(stock_name: str) -> str | None:
    with open(r"Companies_list.json", "r") as file:
        data = json.load(file)
    for stock in data:
        if (stock_name.upper() in stock["name"] or
                stock_name in stock["name"] or
                stock_name in stock["trading_symbol"] or
                stock["name"].upper() in stock_name or
                stock["name"] in stock_name):
            name = stock["instrument_key"]
            return f"{name}"

def get_past_data(stock_name: str) -> list:
    api_version = '2.0'

    api_instance = upstox_client.HistoryApi()
    instrument_key = get_instrument_key_from_stock_name(stock_name)
    interval = 'day'
    to_date = datetime.date.today().strftime("%Y-%m-%d")
    #to_date = (datetime.date.today() + datetime.timedelta(days=8)).strftime('%Y-%m-%d')

    price = []

    api_response = api_instance.get_historical_candle_data(instrument_key, interval, to_date, api_version).data.candles[:120]

    for i in api_response:
        price.append(i[4])
    return price

