import streamlit as st
import pandas as pd
import pandas_datareader as data
from datetime import datetime
import numpy as np
from yahooquery import Ticker


st.subheader("Stock Ticker")
if 'user_input_stock' not in st.session_state:
    st.session_state.user_input_stock = ''
st.session_state.user_input_stock = st.text_input('Enter Stock Ticker',"GOOG", key="key").upper()
st.write("*Current Ticker* :",st.session_state.user_input_stock)
ticker = Ticker(st.session_state.get('user_input_stock'))
st_data = ticker.history(period="1y", interval="1d")
df = pd.DataFrame(st_data)
current_price = df['close'].iloc[-1]

st.write("")

st.subheader("Index Ticker",)
if 'user_input_mkt' not in st.session_state:
    st.session_state.user_input_mkt = ''
today = datetime.today().strftime('%Y-%m-%d')
st.session_state.user_input_mkt = st.text_input('Enter Market Ticker', "^GSPC", key="key_mkt").upper()
st.write("*Current Index Ticker* : ",st.session_state.user_input_mkt)

st.write("")
st.metric("Price", current_price)
