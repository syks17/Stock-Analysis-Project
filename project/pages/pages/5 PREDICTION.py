import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime
import numpy as np
from yahooquery import Ticker
import pandas_datareader as web
import datetime
from prophet import Prophet


ticker = Ticker(st.session_state.get('user_input_stock'))
st_data = ticker.history(period="10y", interval="1d")
st_data = st_data.reset_index()
st.write("Historical Data [Last 10 Days]")
st.write(st_data.tail(10))

df = st_data[['date','close']]
df.columns = ['ds','y']
def clean_datetime(val):
    try:
        if isinstance(val, datetime.datetime):
            return val.replace(tzinfo=None)
        parsed = pd.to_datetime(val, utc=False, errors='coerce')
        if parsed is not pd.NaT:
            return parsed.tz_localize(None) if parsed.tzinfo else parsed
        return val
    except Exception:
        return val
        
df['ds'] = df['ds'].apply(clean_datetime)
df['ds'] = pd.to_datetime(df['ds'], errors='coerce')

prophet1 = Prophet(daily_seasonality=True)
prophet1.fit(df)
years = st.slider("Select forecast period (years)", 1, 5, 1)  # min=1, max=5, default=2
period_days = years * 365
future_dates = prophet1.make_future_dataframe(periods=period_days)
predictions = prophet1.predict(future_dates)

fig, ax = plt.subplots()
ax.plot(df['ds'], df['y'], label="Actual")
ax.plot(predictions['ds'], predictions['yhat'], label="Forecast", alpha=0.7)
ax.fill_between(predictions['ds'], predictions['yhat_lower'], predictions['yhat_upper'], color='gray', alpha=0.2)
ax.set_title("Actual vs Forecast")
ax.legend()
st.pyplot(fig)

fig = prophet1.plot(predictions)
ax = fig.gca()
ax.set_title('Forecasted Trends with Confidence Interval', fontsize=16)
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.grid(True, linestyle='--', alpha=0.6)
st.pyplot(fig)

st.write("")
returns = df['y'].pct_change().dropna()
volatility = returns.std() * (252**0.5)
st.metric("Volatility", f"{volatility*100:.2f}%")
st.write("")

st.subheader("Forecasted Data [Last 10 Days]")
st.dataframe(predictions[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(10))
