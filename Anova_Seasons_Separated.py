import pandas as pd

def filter_fall():
    df = pd.read_csv('SeasonANOVA.csv')
    fall_data = df[df['season'] == 'fall']
    fall_data.to_csv('ANOVA_fall.csv', index=False)
    print('Fall has its own csv file')

def filter_spring():
    df = pd.read_csv('SeasonANOVA.csv')
    fall_data = df[df['season'] == 'spring']
    fall_data.to_csv('ANOVA_spring.csv', index=False)
    print('spring has its own csv file')

def filter_summer():
    df = pd.read_csv('SeasonANOVA.csv')
    fall_data = df[df['season'] == 'summer']
    fall_data.to_csv('ANOVA_summer.csv', index=False)
    print('summer has its own csv file')

def filter_winter():
    df = pd.read_csv('SeasonANOVA.csv')
    fall_data = df[df['season'] == 'winter']
    fall_data.to_csv('ANOVA_winter.csv', index=False)
    print('winter has its own csv file')

#run files 
filter_fall()
filter_spring()
filter_summer()
filter_winter() 