import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def reading_data():
    df = yf.download('BTC-USD', start='2019-01-01')
    closing_price = df['Adj Close']

    window_size = 200

    sma_values = np.zeros_like(closing_price)

    for i in range(window_size, len(closing_price)):
        sma_values[i] = np.mean(closing_price[i - window_size:i])

    df['SMA'] = sma_values

    print(df[['Adj Close', 'SMA']].to_string())

    plt.figure(figsize=(14, 7))
    plt.plot(df['Adj Close'], label='Adjusted Close', color='blue')
    plt.plot(df['SMA'], label='SMA', linestyle='--', color='red')
    plt.title('BTC-USD Adjusted Close Price vs SMA')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()


reading_data()



