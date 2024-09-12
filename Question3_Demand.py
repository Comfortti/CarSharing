import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('CarSharing.csv')

# Convert the 'timestamp' column to datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Extract the 'temp' column
demand_data = df['demand']

# Plot 'temp' against dates
plt.figure(figsize=(10, 6))
plt.plot(df['timestamp'], demand_data)
plt.title('Demand Over Time')
plt.xlabel('Date')
plt.ylabel('Demand')
plt.grid(True)
plt.show()
