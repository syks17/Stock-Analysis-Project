import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime
import numpy as np
from yahooquery import Ticker


user_stock = st.session_state.get('user_input_stock')
st.subheader(user_stock)
st.title("Capital Asset Pricing Model")

today = datetime.today().strftime('%Y-%m-%d')


period_days = st.selectbox("Select period (beta)", ['5y','1y', '2y', '10y', 'max'])
ticker = Ticker(st.session_state.get('user_input_stock'))
st_data = ticker.history(period=period_days, interval="1d")
df = pd.DataFrame(st_data)

ticker_mkt = Ticker(st.session_state.get('user_input_mkt'))
mkt_data = ticker_mkt.history(period=period_days , interval="1d")
df_mkt = pd.DataFrame(mkt_data)


risk_free_rate = st.number_input("Enter Risk-Free Rate (percentage)", 0)/100
st.write(risk_free_rate)

#expected_market_return = st.number_input("Enter expected Market Return(percentage)" , 0)/100
#st.write(expected_market_return)

closing_price_stock = df['close']
closing_price_market = df_mkt['close']

return_stock = closing_price_stock.pct_change().dropna()
return_market = closing_price_market.pct_change().dropna()

min_len = min(len(return_stock), len(return_market))
s1_truncated = return_stock[:min_len]
s2_truncated = return_market[:min_len]

cov_matrix = np.cov(s1_truncated, s2_truncated)
beta = cov_matrix[0, 1] / cov_matrix[1, 1]

st.write("")
st.metric('BETA',beta.round(2))


st.write("")
st.write("")
expected_market_return = return_market.mean() * 252 
expected_return = risk_free_rate + beta * (expected_market_return - risk_free_rate)
st.metric("Expected Return (CAPM)", f"{expected_return * 100:.2f}%")

st.write("")
fig1 = plt.figure(figsize=(12, 6))
sns.regplot(x=s2_truncated, y=s1_truncated, line_kws={"color": "red"})
plt.title("Security Characteristic Line")
plt.grid(True)
plt.xlabel("Market Returns")
plt.ylabel("Stock Returns")
st.pyplot(fig1)

st.write("")
st.write("")
st.write("")
fig, ax = plt.subplots()
sns.histplot(return_stock, color='blue', label='Stock', kde=True)
sns.histplot(return_market, color='orange', label='Market', kde=True)
ax.set_title('Return Distributions')
ax.legend()
st.pyplot(fig)