import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as data
import seaborn as sns
from datetime import datetime
import numpy as np
from yahooquery import Ticker

st.subheader("Stock Ticker")
if 'user_input_stock' not in st.session_state:
    st.session_state.user_input_stock = ''

today = datetime.today().strftime('%Y-%m-%d')
st.session_state.user_input_stock = st.text_input('Enter Stock Ticker',"AAPL", key="key").upper()

st.write("*Current Ticker* :",st.session_state.user_input_stock)



st.write("")



st.subheader("Index Ticker",)
if 'user_input_mkt' not in st.session_state:
    st.session_state.user_input_mkt = ''

today = datetime.today().strftime('%Y-%m-%d')
st.session_state.user_input_mkt = st.text_input('Enter Market Ticker', "^GSPC", key="key_mkt").upper()

st.write("*Current Index Ticker* : ",st.session_state.user_input_mkt)

st.write("")
st.write("")
st.warning("Coming back to HOME page will reset your entries to default")