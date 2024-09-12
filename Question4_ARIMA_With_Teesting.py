import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot

# Load CSV into DataFrame
df = pd.read_csv('CarSharing.csv')

# Convert 'timestamp' column to datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Set 'timestamp' column as index
df.set_index('timestamp', inplace=True)

# Extract 'demand' column
demand = df['demand']

#Checking stanarity
result = adfuller(demand)
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])

#Differencing the series and checking stationarity 
demand_diffed = demand.diff().dropna()
result_diff = adfuller(demand_diffed)
print('ADF Statistic after differencing once: %f' % result_diff[0])
print('p-value after differencing once: %f' % result_diff[1])

#Second differencing 
demand_diff_again = demand_diffed.diff().dropna()
result_diff_again = adfuller(demand_diff_again)
print('ADF Statistic after differencing two times: %f' % result[0])
print('p-value after differencing to times: %f' % result[1])


#because the p-value is smaller than 0.05, we can reject the null hypothesis that the series is non-stationary 
#the time series is stationary
#the further differencing produces stionary time series' too, note that the ADF reverts to the original in the second differencing  
#therefore we can set d to 0 since we did not need to difference the series. 

# Setting the value of p in the ARIMA model. We need to check the PACF plot to see how many
# significant lags we have

df_P = pd.DataFrame(demand.values, columns=['value'])
plt.rcParams.update({'figure.figsize':(9,3), 'figure.dpi':120})
fig, axes = plt.subplots(1, 2, sharex=True)
axes[0].plot(df_P.diff().value)
axes[0].set_title('1st Order Differencing')

axes[1].set(ylim=(0,1.2))
plot_pacf(df_P.diff().value.dropna(), lags=2, ax=axes[1])
plt.show()

#As we can see from the PACF plot, lag=0 give 100%, lag=1 gives roughly 48% and lag=2 gives roughly -0.05%
#the lag 1 is quite high, meaning there is a strong correlation
#lag at 2 is negative and quite low, meaning little correlation
#therefore p should equal 1, to include this observation in the ARIMA model 

df_Q = pd.DataFrame(demand.values, columns=['value'])
plt.rcParams.update({'figure.figsize':(9,3), 'figure.dpi':120})
fig, axes = plt.subplots(1, 2, sharex=True)
axes[0].plot(df_Q.diff().value)
axes[0].set_title('1st Order Differencing')

axes[1].set(ylim=(0,1.2))
plot_acf(df_Q.diff().value.dropna(), lags=3, ax=axes[1])
plt.show()

#As we can see from the ACF plot, autocorrelation is 100% which is expected 
# lag 1 has an AC of roughly 45%, lag 2 of approx 15% and lag 3 of -10%
# using the lag that is still relatively high, the q should be 2 

#training the data 
#70% for training and 30% for testing 
train_size = int(len(df) * 0.7)
train, test = df.demand[:train_size], df.demand[train_size:]

#1,0,2 ARIMA(p,d,q) model 
model = ARIMA(train, order=(1,0,2))
model_fit = model.fit()
print(model_fit.summary())

#plot residual errors 
residuals = pd.DataFrame(model_fit.resid)
fig, ax = plt.subplots(1,2)
residuals.plot(title='Residuals', ax=ax[0])
residuals.plot(kind='kde',title='Density', ax=ax[1])
plt.show()

# Forecast
forecast_values = model_fit.forecast(steps=len(test))
forecast_index = pd.date_range(start=test.index[0], periods=len(test), freq='D')
forecast = pd.Series(forecast_values, index=forecast_index)

# Calculate weekly average demand rate for the forecasted period
# Assuming each data point corresponds to a day, we can resample the data to weekly frequency and calculate the mean
forecast_weekly_avg = forecast.resample('W').mean()

# Plot the forecast and the actual values for the overlapping period
plt.plot(test.index, test.values, color='pink', label='Test Data')
plt.plot(forecast_weekly_avg.index[:len(test)], forecast_weekly_avg[:len(test)], color='red', label='Forecasted Weekly Average')
plt.legend()
plt.title('ARIMA Forecast: Weekly Average Demand Rate')
plt.xlabel('Date')
plt.ylabel('Demand Rate')
plt.show()