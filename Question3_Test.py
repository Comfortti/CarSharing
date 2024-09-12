import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

# Load CSV into DataFrame
df = pd.read_csv('CarSharing.csv')

# Convert 'timestamp' column to datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Set 'timestamp' column as index
df.set_index('timestamp', inplace=True)

# Perform seasonal decomposition on 'temp'
result = seasonal_decompose(df['temp'], model='additive', period=24)  # assuming hourly data with daily seasonality

# Visualize decomposition
plt.figure(figsize=(10, 8))
result.plot()
plt.show()
