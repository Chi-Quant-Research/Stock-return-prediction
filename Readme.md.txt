# Stock Return Prediction using Machine Learning

## Overview
Financial markets are notoriously difficult to predict due to their noisy and dynamic nature. This project implements a machine learning pipeline to predict short-term stock price movements using technical indicators. 

The goal is to demonstrate how predictive models, specifically **Random Forest**, can be applied to financial time series within a reproducible research framework.

---

## Key Visualization
Below is the core output of the analysis, showing the historical price trends and engineered features:

![Stock Price with Moving Averages](stock_price_with_moving_averages.png)

*Figure 1: Apple Inc. (AAPL) Closing Prices with 10-day and 50-day Moving Averages.*

---

## Methodology

### 1. Data Collection & Feature Engineering
Data is retrieved via the `yfinance` API (Apple Inc., 2018–Present). Key features include:
* **MA10 & MA50:** Short and medium-term momentum indicators.
* **Rolling Volatility:** 10-day standard deviation to capture risk dynamics.

### 2. Machine Learning Model
We employ a **Random Forest Classifier** to predict the direction of the next trading day’s return (Binary Classification: 1 for Increase, 0 for Decrease).
* **Train/Test Split:** 70/30 (Chronological split to avoid look-ahead bias).
* **Model Accuracy:** Results typically range between 55–60%, consistent with the *Efficient Market Hypothesis*.

---

## Project Structure
```text
stock-return-prediction
│
├── stock_prediction_ml.py    # Main Python script
├── requirements.txt         # Project dependencies
├── README.md                # Project documentation
└── stock_price_with_moving_averages.png  # Generated visualization
