def darvas_logic_old(stock_price_list: list) -> bool | None:

    buy_recommendation = True
    UPPER_LIMIT_PERCENT = 3
    LOWER_LIMIT_PERCENT = 3


    price_list = stock_price_list

    ltp = float(price_list[0])
    UPPER_LIMIT = ltp / UPPER_LIMIT_PERCENT
    LOWER_LIMIT = ltp / LOWER_LIMIT_PERCENT

    difference_list = []
    for count in range(1, len(price_list)):
        difference_list.append(round(price_list[count - 1] - price_list[count], 2))

    for difference in difference_list[1:]:
        if UPPER_LIMIT >= difference >= LOWER_LIMIT:
            continue
        else:
            break

    if difference_list[0] >= UPPER_LIMIT:
            return buy_recommendation
    else:
        buy_recommendation = False
        return buy_recommendation


def darvas_logic(stock_name: str, price_list: list) -> dict:
    breakout_stocks = {}

    stock = stock_name
    price_list = price_list
    box_stocks = True

    #check if stock is in box
    UPPER_LIMIT_PERCENT = 5
    UPPER_LIMIT = (UPPER_LIMIT_PERCENT * price_list[0]) / 100
    LOWER_LIMIT_PERCENT = 5
    LOWER_LIMIT = -(LOWER_LIMIT_PERCENT * price_list[0]) / 100

    for price in price_list[1:-1]:
        if price - price_list[0] < LOWER_LIMIT:
            #print("Lower bound crossed")
            box_stocks = False
            break
        if price - price_list[0] > UPPER_LIMIT:
            #print(stock)
            #print("Upper bound crossed")
            box_stocks = True
            break

    if box_stocks == True:
        #check for breakout
        BREAKOUT_LIMIT_PERCENT = 5
        BREAKOUT_LIMIT = (BREAKOUT_LIMIT_PERCENT * price_list[-2]) / 100
        #print(f"{price_list[-2]}\t{price_list[-1]}\t{price_list[-2] - price_list[-1]}\t{BREAKOUT_LIMIT}")
        if price_list[-2] - price_list[-1] > BREAKOUT_LIMIT:
             breakout_stocks[stock] = price_list[0]


    return breakout_stocks