import pandas as pd
from scipy.stats import f_oneway

# Read the CSV file
df = pd.read_csv('CarSharing.csv')

# Filter the demands for the weather
clear_demands = df[df['weather'] == 'Clear or partly cloudy']['demand'].tolist()
mist_demands = df[df['weather'] == 'Mist']['demand'].tolist()
lightrain_demands = df[df['weather'] == 'Light snow or rain']['demand'].tolist()
heavyrain_demands = df[df['weather'] == 'heavy rain/ice pellets/snow + fog']['demand'].tolist()

#conduct the one-way ANOVA
results = f_oneway(clear_demands, mist_demands, lightrain_demands, heavyrain_demands)
print(results)