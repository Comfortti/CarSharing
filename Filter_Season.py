import numpy as np 
import pandas as pd 

def filter_season():
    df = pd.read_csv('CarSharing.csv')

    filtering = df[['season', 'demand']]
    sorting = filtering.sort_values(by='season')

    sorting.to_csv('SeasonANOVA.csv', index=False)
    print('CarSharing has been filtered and sorted for ANOVA')

#run file
filter_season()