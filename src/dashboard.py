import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def build_dashboard(ohlc_df: pd.DataFrame, metrics_df: pd.DataFrame):

    # PAGE
    st.set_page_config(
        page_title="Stocks Dashboard",
        layout="wide"
    )

    st.title("Stocks Dashboard")

    # SIDEBAR
    tickers = sorted(metrics_df["Ticker"].unique())

    selected_ticker = st.sidebar.selectbox(
        "Select Ticker",
        tickers
    )

    # FILTER
    ticker_df = ohlc_df[
        ohlc_df["Ticker"] == selected_ticker
    ].copy()

    # table view -> latest first
    ticker_df = ticker_df.sort_values(
        "Date",
        ascending=False
    )

    # chart view -> oldest first
    chart_df = ticker_df.sort_values(
        "Date",
        ascending=True
    )

    metrics = metrics_df[
        metrics_df["Ticker"] == selected_ticker
    ].iloc[0]

    # METRICS ROW
    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "YTD Return",
        f"{metrics['YTD Return']:.2%}"
    )

    col2.metric(
        "Sharpe",
        f"{metrics['Sharpe']:.2f}"
    )

    col3.metric(
        "Beta",
        f"{metrics['Beta']:.2f}"
    )

    col4.metric(
        "Volatility",
        f"{metrics['Volatility Annualized']:.2%}"
    )

    col5.metric(
        "RSI",
        f"{metrics['RSI']:.1f}"
    )

    # CANDLESTIC
    fig = go.Figure()

    fig.add_trace(
        go.Candlestick(
            x=chart_df["Date"],
            open=chart_df["Open"],
            high=chart_df["High"],
            low=chart_df["Low"],
            close=chart_df["Close"],
            name="Price"
        )
    )

    # SMA 20
    fig.add_trace(
        go.Scatter(
            x=chart_df["Date"],
            y=chart_df["SMA_20"],
            name="SMA 20"
        )
    )

    # SMA 50
    fig.add_trace(
        go.Scatter(
            x=chart_df["Date"],
            y=chart_df["SMA_50"],
            name="SMA 50"
        )
    )

    # EMA 9
    fig.add_trace(
        go.Scatter(
            x=chart_df["Date"],
            y=chart_df["EMA_9"],
            name="EMA 9"
        )
    )

    fig.update_layout(
        title=f"{selected_ticker} Price Chart",
        height=700,
        xaxis_rangeslider_visible=False
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    # RETURNS + VOLUME
    col1, col2 = st.columns(2)

    with col1:

        returns_fig = px.line(
            chart_df,
            x="Date",
            y="Returns",
            title="Daily Returns"
        )

        st.plotly_chart(
            returns_fig,
            width="stretch"
        )

    with col2:

        volume_fig = px.bar(
            chart_df,
            x="Date",
            y="Volume",
            title="Volume"
        )

        st.plotly_chart(
            volume_fig,
            width="stretch"
        )

    # RSI
    rsi_fig = px.line(
        chart_df,
        x="Date",
        y="RSI",
        title="RSI"
    )

    rsi_fig.add_hline(y=70)
    rsi_fig.add_hline(y=30)

    st.plotly_chart(
        rsi_fig,
        width="stretch"
    )

    # STOCK SCREENER TABLE
    st.subheader("Metrics Overview")

    display_cols = [
        "Ticker",
        "YTD Return",
        "Sharpe",
        "Beta",
        "Correlation",
        "RSI",
        "Volatility Annualized"
    ]

    st.dataframe(
        metrics_df[display_cols]
        .sort_values("Sharpe", ascending=False),
        width="stretch",
        hide_index=True
    )

    # RAW DATA
    with st.expander("Show OHLC Data"):

        st.dataframe(
            ticker_df,
            width="stretch",
            hide_index=True
        )