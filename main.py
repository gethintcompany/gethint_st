import pandas as pd

from stock_name_scrapper import get_good_stocks_bs
from upstox import get_past_data
from algo import darvas_logic_old, darvas_logic

def main():
    stocks_to_buy = {}
    caught_in_error = []
    good_stocks = get_good_stocks_bs()

    for stock in good_stocks:
        try:
            stock_price_list = get_past_data(stock_name=stock)
            result = darvas_logic_old(stock_price_list)
            if result:
                stocks_to_buy[stock] = stock_price_list[0]
            else:
                pass
        except:
            caught_in_error.append(stock)
            continue
        stocks_to_buy = pd.DataFrame(stocks_to_buy)
    return good_stocks, caught_in_error, stocks_to_buy

#print(main())