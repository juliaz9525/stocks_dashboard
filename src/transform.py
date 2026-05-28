import pandas as pd
import numpy as np

def transform_data(data: dict)-> dict:
    processed_data = []
    metrics_dfs = []
    rf_df = data["^IRX"].copy()
    rf_df["Date"] = pd.to_datetime(rf_df["Date"])
    rf_df = rf_df.set_index("Date")

    rf_annual = rf_df["Close"] / 100
    rf_daily = rf_annual / 252

    spy_df = data["SPY"].copy()
    spy_df["Date"] = pd.to_datetime(spy_df["Date"])
    spy_df = spy_df.set_index("Date")

    spy_returns = spy_df["Close"].pct_change()
    for ticker, df in data.items():
        ##
        if ticker == "^IRX":
            continue
        # OHLC Related
        df["Date"] = pd.to_datetime(df["Date"])
        df = df.set_index("Date")
        df["Returns"] = df["Close"].pct_change()
        df["SMA_20"] = df["Close"].rolling(20).mean()
        df["SMA_50"] = df["Close"].rolling(50).mean()
        df["SMA_100"] = df["Close"].rolling(100).mean()
        df["SMA_200"] = df["Close"].rolling(200).mean()
        df["EMA_9"] = df["Close"].ewm(span=9).mean()
        df["EMA_20"] = df["Close"].ewm(span=20).mean()
        df["Volume_MA"] = df["Volume"].rolling(20).mean()
        df["Relative_Volume"] = df["Volume"] / df["Volume_MA"]
        excess_returns = df["Returns"].sub(rf_daily, axis=0)

        delta = df["Close"].diff()
        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)
        avg_gain = gain.rolling(14).mean()
        avg_loss = loss.rolling(14).mean()
        rs = avg_gain / avg_loss
        df["RSI"] = 100 - (100 / (1+rs))

        # Metrics
        sharpe = (excess_returns.mean() / excess_returns.std()) * np.sqrt(252)
        covariance = df["Returns"].cov(spy_returns)
        correlation= df["Returns"].corr(spy_returns)
        volatility_annualized = df["Returns"].std() * np.sqrt(252)
        beta = df["Returns"].cov(spy_returns) / spy_returns.var()
        high_52w = df["Close"].rolling(252).max()
        high_distance_52w = (df["Close"] / high_52w).iloc[-1]
        latest_rsi = df["RSI"].iloc[-1]
        # YTD
        current_year = df.index[-1].year
        ytd_df = df[df.index.year == current_year]
        ytd_return = (
                             ytd_df["Close"].iloc[-1] /
                             ytd_df["Close"].iloc[0]
                     ) - 1

        # Append
        metric = pd.DataFrame({
            "Ticker": [ticker],
            "Sharpe": [sharpe],
            "Covariance": [covariance],
            "Correlation": [correlation],
            "RSI": [latest_rsi],
            "Volatility Annualized": [volatility_annualized],
            "Beta": [beta],
            "YTD Return": [ytd_return],
            "52W High": [high_52w.iloc[-1]],
            "52W High Distance": [high_distance_52w]
        })
        df = df.reset_index()
        df["Date"] = df["Date"].dt.date
        df = df.sort_values("Date", ascending=False)
        processed_data.append(df)
        metrics_dfs.append(metric)

    processed_data = pd.concat(processed_data)
    metrics_dfs = pd.concat(metrics_dfs)

    return {
        "processed_data": processed_data,
        "metrics_dfs": metrics_dfs
    }