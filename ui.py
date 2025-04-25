import streamlit as st

from main import main


button_press = st.button("Press to get stocks to buy")

if button_press:
    good_stocks, error_in_names, stocks_to_buy = main()

    st.write(f"These are the {len(good_stocks)} stocks that are scraped from moneycontrol\n{good_stocks}")
    st.write(f"These {len(error_in_names)} names arent found in the upstox data. Yo will have to modify the names\n {error_in_names}")
    st.write(stocks_to_buy)