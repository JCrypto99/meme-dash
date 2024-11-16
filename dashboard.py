import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# Define API keys
etherscan_key = '6NMUVWW5DEVRZFN66V2GY1QFFTNV48WQZ2'
lunarcrush_key = '0d9pyy7o3qhajqdsy24s87z475m3kd9iyt2bcmlw9'
whale_alert_key = 'ISgaosmbus9hlSkGpYzmHdmhdItuJ8bF'

# Function to fetch data from Whale Alert
def fetch_whale_alert_data():
    endpoint = 'https://api.whale-alert.io/v1/transactions'
    params = {
        'api_key': whale_alert_key,
        'min_value': 100000,
        'start': 0,
        'limit': 10  # Limit for testing
    }
    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        return response.json().get('transactions', [])
    return []

# Function to fetch data from LunarCrush
def fetch_lunarcrush_data():
    endpoint = f'https://api.lunarcrush.com/v2'
    params = {
        'data': 'assets',
        'key': lunarcrush_key,
        'symbol': 'BTC'  # Replace with any symbol for testing
    }
    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        return response.json().get('data', [])
    return []

# Main Dashboard
st.title("Crypto Memecoin Tracker")

# Whale Alert Section
st.header("Whale Transactions")
whale_data = fetch_whale_alert_data()
if whale_data:
    df_whale = pd.DataFrame(whale_data)
    st.dataframe(df_whale[['blockchain', 'symbol', 'amount', 'to_owner']])
    fig_whale = px.bar(df_whale, x='symbol', y='amount', title="Whale Transactions by Token")
    st.plotly_chart(fig_whale)
else:
    st.write("No whale transactions available.")

# LunarCrush Section
st.header("Social Sentiment (LunarCrush)")
lunar_data = fetch_lunarcrush_data()
if lunar_data:
    df_lunar = pd.DataFrame(lunar_data)
    st.dataframe(df_lunar[['symbol', 'social_volume', 'social_score']])
    fig_lunar = px.bar(df_lunar, x='symbol', y='social_volume', title="Social Volume by Token")
    st.plotly_chart(fig_lunar)
else:
    st.write("No social data available.")

st.write("More integrations coming soon!")
