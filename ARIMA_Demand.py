import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np

# Load CSV into DataFrame
df = pd.read_csv('CarSharing.csv')

# Convert 'timestamp' column to datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Set 'timestamp' column as index
df.set_index('timestamp', inplace=True)

# Extract 'demand' column
demand = df['demand']

# Split data into training and testing sets
train_size = int(len(demand) * 0.7)  # 70% for training
train, test = demand[:train_size], demand[train_size:]

# Fit ARIMA model
model = ARIMA(train, order=(1,1,1))  # ARIMA(p,d,q) with p=5, d=1, q=0
model_fit = model.fit()

# Make predictions
predictions = model_fit.forecast(steps=len(test))

# Evaluate model performance
mse = mean_squared_error(test, predictions)
rmse = np.sqrt(mse)
print(f'Root Mean Squared Error (RMSE): {rmse}')

# Predict weekly average demand rate
weekly_avg_demand = model_fit.forecast(steps=7*24, alpha=0.05)  # predict 7 days worth of hourly data with 95% confidence interval
weekly_avg_demand = weekly_avg_demand.mean()  # take average for each day
print("Weekly average demand rate predictions:")
print(weekly_avg_demand)

