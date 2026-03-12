import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Create folders
os.makedirs("data", exist_ok=True)
os.makedirs("results", exist_ok=True)

# Download stock data
ticker = "AAPL"
data = yf.download(ticker, start="2018-01-01")

# Feature engineering
data["Return"] = data["Close"].pct_change()

data["MA10"] = data["Close"].rolling(10).mean()
data["MA50"] = data["Close"].rolling(50).mean()

data["Volatility"] = data["Return"].rolling(10).std()

data = data.dropna()

# Target variable (1 if price goes up tomorrow)
data["Target"] = np.where(data["Return"].shift(-1) > 0, 1, 0)

features = ["MA10","MA50","Volatility"]

X = data[features]
y = data["Target"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.3,shuffle=False
)

# Random Forest model
model = RandomForestClassifier(n_estimators=100)

model.fit(X_train,y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test,predictions)

print("Model Accuracy:", accuracy)

# Save dataset
data.to_csv("data/stock_features.csv")

# Plot price + moving averages
plt.figure(figsize=(10,6))

plt.plot(data["Close"], label="Price")
plt.plot(data["MA10"], label="MA10")
plt.plot(data["MA50"], label="MA50")

plt.title("Stock Price with Moving Averages")

plt.legend()

plt.savefig("results/price_moving_average.png")

plt.show()