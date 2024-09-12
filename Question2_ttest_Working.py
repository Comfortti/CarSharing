import pandas as pd 
import scipy.stats as stats 

# Read the CSV file
df = pd.read_csv('CarSharing.csv')

#filter the demands for workinngday-yes or workingday-no 
yes_working = df[df['workingday'] == 'Yes']['demand'].tolist()
no_working = df[df['workingday'] == 'No']['demand'].tolist()

results = stats.ttest_ind(yes_working, no_working, equal_var=True)
print(results)