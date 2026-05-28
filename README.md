# Stock Analytics Dashboard

A Python-based stock analytics dashboard built with Streamlit, Pandas, and Plotly.

The project focuses on:

* OHLC market data visualization
* Portfolio and stock performance metrics
* Risk-adjusted return analysis
* Interactive dashboards for financial analysis

Designed as both:

* a portfolio project for finance/data analyst roles
* a foundation for future swing trading and portfolio analytics tools

# Features

## Market Data Processing

* Historical OHLCV data handling
* Daily return calculations
* Risk-free rate integration
* Benchmark comparison (SPY)

## Financial Metrics

The dashboard calculates metrics such as:

* Daily Returns
* Cumulative Returns
* Annualized Volatility
* Sharpe Ratio
* Beta
* RSI (Relative Strength Index)

## Interactive Dashboard

Built with Streamlit and Plotly:

* Candlestick charts
* Performance visualizations
* Metric summary tables
* Interactive filtering and navigation

# Tech Stack

## Languages

* Python

## Libraries

* Pandas
* NumPy
* Plotly
* Streamlit
* yfinance

# Project Structure

```text
project/
│
├── app.py                  # Streamlit dashboard
├── get_data.py          # Data acquisition
├── transformations.py      # Financial calculations and metrics
├── dashboard.py            # Plotly visualizations
├── load_yaml.py            # Loading yaml data
├── stocks.yaml             # Stocks and intervals values
├── requirements.txt
└── README.md
```

# Metrics Overview

## Sharpe Ratio

Measures risk-adjusted returns.

## Annualized Volatility

Annualized standard deviation of returns.

## Beta

Measures sensitivity relative to the benchmark.

# Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

Install dependencies:

```bash
pip install -r requirements.txt
```


# Running the Dashboard

Start the Streamlit app:

```bash
streamlit run app.py
```

The dashboard will open locally in your browser.

# Example Workflow

1. Load historical stock data
2. Calculate returns and technical metrics
3. Compare performance against SPY
4. Visualize OHLC data and risk metrics
5. Analyze volatility and drawdowns

# Future Improvements

Planned extensions:

* Additional technical indicators

* Portfolio tracking view

* Improved filtering and stock selection

* Better dashboard layout and usability

# Purpose

This project was created to practice:

* working with financial market data
* building dashboards with Streamlit
* data analysis with Pandas
* calculating basic stock performance metrics
* creating visualizations with Plotly

# Screenshots of runnnign dashboard for period of 1 year, interval 1 day
<img width="1440" height="785" alt="image" src="https://github.com/user-attachments/assets/eb82bcd4-1e39-412a-85ae-6d35dc1b8a7e" />
<img width="1440" height="785" alt="image" src="https://github.com/user-attachments/assets/f24502b3-3682-471e-a2c8-bc30e987ba46" />


