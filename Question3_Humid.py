import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('CarSharing.csv')

# Convert the 'timestamp' column to datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Extract the 'temp' column
hum_data = df['humidity']

# Plot 'temp' against dates
plt.figure(figsize=(10, 6))
plt.plot(df['timestamp'], hum_data)
plt.title('Humiidity Over Time')
plt.xlabel('Date')
plt.ylabel('Humidity')
plt.grid(True)
plt.show()
