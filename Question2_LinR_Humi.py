import pandas as pd 
from sklearn.feature_selection import f_regression
from sklearn.feature_selection import SelectKBest

df = pd.read_csv('CarSharing.csv')
x = df[['humidity']]
y = df['demand']

test = SelectKBest(score_func=f_regression, k=2)
fit = test.fit(x,y)

results = pd.DataFrame({'Humidity': x.columns, 'p-value': fit.pvalues_})
print(results)