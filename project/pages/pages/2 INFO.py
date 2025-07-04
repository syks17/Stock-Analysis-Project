import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime
import numpy as np
from yahooquery import Ticker



user_stock = st.session_state.get('user_input_stock')
period_days = st.selectbox("Select period", ['5y','1y', '2y','10y','max'])
today = datetime.today().strftime('%Y-%m-%d')
ticker = Ticker(st.session_state.get('user_input_stock'))
st_data = ticker.history(period=period_days, interval="1d")
df = pd.DataFrame(st_data)


st.write("")


price_data , Info , = st.tabs(["Price data","Info"])
with price_data:
    col1,col2,col3 = st.columns(3)
    daily_change = df['close'].iloc[-1] - df['close'].iloc[-2]
    col1.metric('Daily Change',str(round(df['close'].iloc[-1],2)), str(round(daily_change,2)))


    st.subheader('Closing Price Chart')
    closing_price = df['close']
    fig = plt.figure(figsize=(12, 6))
    sns.lineplot(x='date', y='close', data=df, label='Closing Price')
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title("Closing Price Over Time")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    st.pyplot(fig)


    df['MA100'] = df['close'].rolling(window=100).mean()
    df['MA200'] = df['close'].rolling(window=200).mean()

    st.subheader("100 Days MA vs 200 Days MA")
    fig2 = plt.figure(figsize=(17,8))
    sns.lineplot(x='date', y='close', data=df , label = 'closing price')
    sns.lineplot(x='date', y='MA100', data = df , label= '100 days Moving Avg',linestyle = '--' , color = 'Orange')
    sns.lineplot(x='date', y='MA200', data = df , label= '200 days Moving Avg',linestyle = '--' , color = 'green')
    plt.xlabel('date')
    plt.ylabel('Price')
    plt.grid(True)
    plt.legend()
    st.pyplot(fig2)


with Info:
    st.subheader(user_stock)
    if user_stock:
        try:
            stock = Ticker(user_stock)

            profile = stock.asset_profile.get(user_stock, {})
            long_summary = profile.get("longBusinessSummary", "No summary available.")
            sector = profile.get("sector", "N/A")
            website = profile.get("website", "N/A")


            st.write(long_summary)
            st.markdown(f"**Sector**: {sector}")
            st.markdown(f"**Website**: {website}")
     

        except Exception as e:
            st.error(f"Error: {e}")

    
    


