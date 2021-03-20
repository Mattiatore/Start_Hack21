def large_price_change(series, threshold=3, window_day=1, running_mean=3, contract_type='hourly'):
    """[Alert for large price changes]

    Args:
        series ([type], optional): [time series]. Defaults to None.
        threshold (int, optional): [price change (e.g. 10% = 0.1) threshold]. Defaults to 3.
        window_day (int, optional): [window of comparison in days (comparing the current price vs. 1 day before)]. Defaults to 1.
        running_mean (int, optional): [running mean in order to prevent too many alerts]. Defaults to 3.
        contract_type (str, optional): ['hourly' or 'quarterly' contracts]. Defaults to 'hourly'.

    Returns:
        [list]: [list of {0,1} where 0: no alert, 1: alert, len(list) != len(series)]
    """

    if contract_type == 'hourly':
        time = 24
    elif contract_type == 'quarterly':
        time = 24*60 / 15
    start = 0 #start index
    end = int(time*window_day) #end of index: depending on how many days we want to include
    
    #We create a new time series with a running mean to smooth the values
    series_running = series.rolling(window=3).mean()

    #empty list of that will be filled with alerts 0: no alert, 1: alert
    alert = []
    
    #We iterate through the time series with the start and end index
    while end < len(series):
        price_change = (series[end]-series_running[start]) / series_running[start]
        if price_change > threshold:
            alert.append(1)
        else: 
            alert.append(0)
        start += 1
        end += 1
    
    return alert


##New alert: Cross-over strategy alert (BUY/SELL)

def cross_over(series, short_term_window=20, long_term_window=50):
    """cross-over Alert

    Args:
        series ([pd.Series]): [Pandas Series object]
        short_term_window (int, optional): [short term moving average window in days]. Defaults to 20.
        long_term_window (int, optional): [long term moving average window in days]. Defaults to 50.
    """

    df = series.to_frame()
    df.columns = ['Price']
    # create short-term simple moving average column
    df['S_SMA'] = df['Price'].rolling(window = short_term_window, min_periods = 1).mean()
    # create long-term simple moving average column
    df['L_SMA'] = df['Price'].rolling(window = long_term_window, min_periods = 1).mean()
    # We create a signal column
    df['Signal'] = 0.0
    df['Signal'] = np.where(df['S_SMA'] > df['L_SMA'], 1.0, 0.0)
    df['Position'] = df['Signal'].diff()

    plt.figure(figsize = (20,10))
    # plot close price, short-term and long-term moving averages 
    df['Price'].plot(color = 'k', label= 'Price') 
    df['S_SMA'].plot(color = 'b',label = '%d-day SMA' % (short_term_window)) 
    df['L_SMA'].plot(color = 'g', label = '%d-day SMA' % (long_term_window))
    # plot ‘buy’ signals
    plt.plot(df[df['Position'] == 1].index, 
            df['S_SMA'][df['Position'] == 1], 
            '^', markersize = 15, color = 'g', label = 'buy')
    # plot ‘sell’ signals
    plt.plot(df[df['Position'] == -1].index, 
            df['S_SMA'][df['Position'] == -1], 
            'v', markersize = 15, color = 'r', label = 'sell')
    plt.ylabel('Price', fontsize = 15 )
    plt.xlabel('Date', fontsize = 15 )
    plt.title('Price Signals for Energy Market', fontsize = 20)
    plt.legend()
    plt.grid()
    plt.show()