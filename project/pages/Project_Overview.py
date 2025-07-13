import streamlit as st

st.subheader('Project Overview')
st.markdown("This is an educational project built using Python and Streamlit. This interactive tool "
    "is designed to help users explore financial data, understand risk-return trade-offs, "
    "and forecast stock prices through a user-friendly interface. It serves as a learning platform "
    "for quantitative finance, data analysis, and web application development.")
st.markdown("""

- This project is for education purposes only.
- The project uses Prophet for Price prediction.
- Going back to the `HOME` page will reset the entered tickers to dafault because of the streamlit refresh feature.
        


            """)

st.subheader("Libraries used:")
st.markdown("""
- streamlit - `App creation`
- matplotlib - `Vizualization`
- pandas - `Data handling`
- seaborn - `Visualization`
- datetime - `Formatting of date`
- numpy - `Data handling`
- yahooquery - `Stock data download`
- pandas-datareader - `Formatting`
- prophet - `For Prediction`
- scikit-learn - `Regression and Beta`
---
""")

st.markdown("""
            

###  Application Pages Overview

The application is divided into the following pages:

            
####  Home

- Users input the **Market Index Ticker** (e.g., ^GSPC for S&P 500) and a **Stock Ticker** (e.g., GOOG for GOOGLE).  
- Fetches historical stock data using `yahooquery`.  
- Sets the context for analysis across the application.

---

####  Info

- Displays essential information about the selected stock such as:
  - Company profile  
  - Sector and website    
  - Recent price data and Key financial metrics 

---

####  CAPM

- Performs **Capital Asset Pricing Model (CAPM)** analysis to estimate the expected return of the stock.  
- Visualizes:
  - Risk-free rate, beta, and market premium  
  - Security Characteristic Line
  - Summary table showing CAPM formula components  

---

####  Prediction

- Uses **Prophet**, a time-series forecasting tool by Meta, to predict future stock prices.  
- Allows users to customize the forecast period.  
- Visualizes 
    -the forecast with upper and lower confidence intervals. 
    -Actual and Forecasted Line
""")
