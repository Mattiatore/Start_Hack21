def large_price_change(series=None, threshold=3, window_day=1, running_mean=3, contract_type='hourly'):
    """[Alert for large price changes]

    Args:
        series ([type], optional): [time series]. Defaults to None.
        threshold (int, optional): [price change (e.g. 10% = 0.1) threshold]. Defaults to 3.
        window_day (int, optional): [window of comparison in days (comparing the current price vs. 1 day before)]. Defaults to 1.
        running_mean (int, optional): [running mean in order to prevent too many alerts]. Defaults to 3.
        contract_type (str, optional): ['hourly' or 'quarterly' contracts]. Defaults to 'hourly'.

    Returns:
        [type]: [description]
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