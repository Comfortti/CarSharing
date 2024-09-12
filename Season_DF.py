import pandas as pd
import numpy as np

# Load the CSV file into a DataFrame
fall_df = pd.read_csv('ANOVA_fall.csv')
winter_df = pd.read_csv('ANOVA_winter.csv')
spring_df = pd.read_csv('ANOVA_spring.csv')
summer_df = pd.read_csv('ANOVA_summer.csv')

ANOVA_df = pd.DataFrame({'fall': fall_df['season'], 'winter': winter_df['season'], 'spring': spring_df['season'], 'summer': summer_df['season'], 'demand': fall_df['demand'] + winter_df['demand'] + spring_df['demand'] + summer_df['demand']})

print(ANOVA_df)
