import yfinance as yf

def get_data_f(stocks, dperiod, dinterval)-> dict:
    data = {}
    for stock in stocks:
        df = yf.download(stock, period=dperiod, interval=dinterval)
        df.columns = df.columns.get_level_values(0)
        df = df.reset_index()
        df["Ticker"] = stock
        data[stock] = df
    print(data)
    return data