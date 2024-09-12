import pandas as pd 
import scipy.stats as stats 

# Read the CSV file
df = pd.read_csv('CarSharing.csv')

#filter the demands for holiday-yes or holiday-no 
yes_Holiday = df[df['holiday'] == 'Yes']['demand'].tolist()
no_holiday = df[df['holiday'] == 'No']['demand'].tolist()

results = stats.ttest_ind(yes_Holiday, no_holiday, equal_var=True)
print(results)