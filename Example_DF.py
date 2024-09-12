import pandas as pd
from scipy.stats import f_oneway

# Read the CSV file
df = pd.read_csv('SeasonANOVA.csv')

# Filter the demands for the 'fall' season
fall_demands = df[df['season'] == 'fall']['demand'].tolist()
winter_demands = df[df['season'] == 'winter']['demand'].tolist()
spring_demands = df[df['season'] == 'spring']['demand'].tolist()
summer_demands = df[df['season'] == 'summer']['demand'].tolist()

#conduct the one-way ANOVA

f_oneway(fall_demands, winter_demands, spring_demands, summer_demands)