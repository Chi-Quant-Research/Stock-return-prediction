# Stock Return Prediction using Machine Learning

## Overview

Financial markets are notoriously difficult to predict due to their noisy and dynamic nature. Nevertheless, machine learning methods have increasingly been applied in empirical finance to detect patterns in historical market data.

This project implements a simple machine learning pipeline to predict short-term stock price movements using technical indicators derived from historical data. The goal is not to produce a trading system, but to demonstrate how predictive models can be applied to financial time series within a reproducible research framework.

The project illustrates the following workflow:

* Financial data acquisition
* Feature engineering using technical indicators
* Machine learning classification
* Model evaluation
* Visualization of financial indicators

This repository is part of a financial analytics portfolio demonstrating applications of data science in empirical finance.

---

# Dataset

Historical daily stock price data is downloaded from **Yahoo Finance** using the `yfinance` API.

**Asset used**

* Apple Inc. (AAPL)

**Time period**

2018 – Present

The dataset contains:

* Daily closing prices
* Daily returns
* Moving averages
* Rolling volatility measures

All engineered features used in the model are saved locally for reproducibility.

---

# Methodology

## 1. Data Collection

Stock price data is retrieved programmatically using the `yfinance` Python package. This ensures that the analysis can be easily replicated with updated data.

---

## 2. Feature Engineering

Several commonly used technical indicators are constructed:

* **10-day Moving Average (MA10)**
* **50-day Moving Average (MA50)**
* **Rolling Volatility (10-day standard deviation of returns)**

These indicators are widely used in empirical trading strategies and capture short-term momentum and risk dynamics.

---

## 3. Target Variable

The model predicts the **direction of the next trading day’s return**.

Target definition:

* **1** → stock price increases the next day
* **0** → stock price decreases the next day

This formulation converts the problem into a binary classification task.

---

## 4. Machine Learning Model

A **Random Forest Classifier** is used to predict the probability that the stock price will increase on the following day.

Reasons for using Random Forest:

* Captures non-linear relationships
* Robust to noise in financial data
* Performs well with small feature sets
* Widely used in applied machine learning research

---

## 5. Model Evaluation

The model is evaluated using **prediction accuracy** on an out-of-sample test dataset.

The dataset is split chronologically to preserve the time-series structure:

* 70% training data
* 30% testing data

This approach avoids look-ahead bias.

---

# Key Results

Example output from the model:

Model Accuracy: ~55–60%

Although the predictive power appears modest, this result is consistent with the **Efficient Market Hypothesis**, which suggests that financial markets incorporate information rapidly and therefore limit predictable patterns in returns.

The purpose of the model is to demonstrate the application of machine learning techniques rather than to generate a profitable trading strategy.

---

# Output

The script produces the following visualization:

![Price and Moving Averages](stock_price_with_moving_averages.png)

*Figure 1: Apple Inc. (AAPL) Closing Prices with 10-day and 50-day Moving Averages.*
---

# Project Structure

```
stock-return-prediction-ml
│
├── data
│   └── stock_features.csv
│
├── results
│   └── price_moving_average.png
│
├── stock_prediction_ml.py
├── requirements.txt
└── README.md
```

---

# How to Run

## 1. Clone the repository

```
git clone https://github.com/yourusername/stock-return-prediction-ml.git
```

## 2. Install dependencies

```
pip install -r requirements.txt
```

## 3. Run the script

```
python stock_prediction_ml.py
```

The script will automatically:

* Download financial data
* Generate features
* Train the machine learning model
* Evaluate prediction accuracy
* Save results and charts

---

# Key Takeaways

This project highlights several important insights about machine learning in financial markets:

* Financial returns are inherently noisy and difficult to predict
* Feature engineering plays a critical role in model performance
* Simple models can still provide useful analytical insights
* Reproducible pipelines are essential in empirical financial research

While this project uses a relatively simple feature set, the framework can be extended to include:

* Additional technical indicators
* Macroeconomic variables
* Alternative machine learning algorithms
* Backtesting of trading strategies

---

# Technologies Used

Python libraries used in this project:

* pandas
* numpy
* scikit-learn
* matplotlib
* yfinance

---

# Disclaimer

This project is intended for educational and research purposes only.

It does not constitute financial advice or investment recommendations.


