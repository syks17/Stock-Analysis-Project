import streamlit as st
import pandas as pd
import pandas_datareader as data
from datetime import datetime
import numpy as np
from yahooquery import Ticker

#STOCK
st.warning("If SSL error occurs Please refresh the page")
st.write("")
st.subheader("Stock Ticker")
if 'user_input_stock' not in st.session_state:
    st.session_state.user_input_stock = ''
st.session_state.user_input_stock = st.text_input('Enter Stock Ticker',"GOOG", key="key").upper()
st.write("*Current Ticker* :",st.session_state.user_input_stock)
ticker = Ticker(st.session_state.get('user_input_stock'))
if ticker:
    try:
        st_data = ticker.history(period="1y", interval="1d")
        df = pd.DataFrame(st_data)
        current_price = df['close'].iloc[-1]
        st.write("Current Price",current_price.round(2))
    except Exception:
        st.error("No data found for the ticker. Please check the ticker symbol.")


st.write("")

#INDEX
st.subheader("Index Ticker",)
if 'user_input_mkt' not in st.session_state:
    st.session_state.user_input_mkt = ''
today = datetime.today().strftime('%Y-%m-%d')
st.session_state.user_input_mkt = st.text_input('Enter Market Ticker', "^GSPC", key="key_mkt").upper()
ticker_mkt = Ticker(st.session_state.get('user_input_mkt'))
st.write("*Current Index Ticker* : ",st.session_state.user_input_mkt)
if ticker_mkt:
    try:
        st_data = ticker_mkt.history(period="1y", interval="1d")
        dfmkt = pd.DataFrame(st_data)
        current_price_mkt = dfmkt['close'].iloc[-1]
        st.write("Current Price",current_price_mkt.round(2))
    except Exception:
        st.error("No data found for the index ticker. Please check the ticker symbol. Make sure to add `^` before the index ticker")

st.write("")



