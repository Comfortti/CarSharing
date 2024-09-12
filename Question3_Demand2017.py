import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

# Load CSV 
df = pd.read_csv('CarSharing.csv')

# Convert 'timestamp' column to pandas' datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Filter data for the year 2017
df_2017 = df[df['timestamp'].dt.year == 2017]

# Set 'timestamp' column as the index
df_2017.set_index('timestamp', inplace=True)

# run seasonal decomposition on 'demandd'
# period is 24 because data is hourly
result = seasonal_decompose(df_2017['demand'], model='additive', period=24) 

# Visualisation
plt.figure(figsize=(10, 8))
result.plot()
plt.show()