import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from scipy.stats import norm

def get_simulation(ticker, time, i):

    name = yf.Ticker(ticker).info['longName']
    data = pd.DataFrame()
    data[ticker] = yf.download(ticker, start='2007-01-01')['Adj Close']

    log_returns = np.log(1 + data.pct_change())

    u = log_returns.mean()
    var = log_returns.var()

    drift = u - (0.5 * var)   # average change of stock value over time
    stdev = log_returns.std()   # measure of dispersion of stock prices from mean

    t_intervals = time
    iterations = i

    daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))

    S0 = data.iloc[-1]

    price_list = np.zeros_like(daily_returns)
    price_list[0] = S0
    
    for t in range(1, t_intervals):
        price_list[t] = price_list[t - 1] * daily_returns[t]


    plt.figure(figsize = (10, 6))
    plt.title("Monte Carlo Simulation for " + name)
    plt.xlabel('Time')
    plt.ylabel('Price')

    plt.plot(price_list)
    plt.show()