import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import StandardScaler

# Load the csv file
df = pd.read_csv("CarSharing.csv")

# need the 'demand' column for prediction
y = df['demand']

# Splitting into train and test sets, 70% for training 
y_train, y_test = train_test_split(y, test_size=0.3, random_state=42)

# Random Forest Regressor
rf_model = RandomForestRegressor(random_state=42)
rf_model.fit(y_train.index.values.reshape(-1, 1), y_train)
rf_pred = rf_model.predict(y_test.index.values.reshape(-1, 1))
rf_mse = mean_squared_error(y_test, rf_pred)
print("Random Forest MSE:", rf_mse)

# Deep Neural Network
dnn_model = Sequential([
    Dense(64, activation='relu', input_shape=(1,)),
    Dense(64, activation='relu'),
    Dense(1)
])

dnn_model.compile(optimizer='adam', loss='mse')
dnn_model.fit(y_train.index.values.reshape(-1, 1), y_train, epochs=50, batch_size=30, verbose=0)
dnn_pred = dnn_model.predict(y_test.index.values.reshape(-1, 1))
dnn_mse = mean_squared_error(y_test, dnn_pred)
print("Deep Neural Network MSE:", dnn_mse)

# Predictions using Random Forest Regressor
rf_predictions = rf_model.predict(y_test.index.values.reshape(-1, 1))

# Predictions using Deep Neural Network
dnn_predictions = dnn_model.predict(y_test.index.values.reshape(-1, 1))

print("Random Forest Predictions:", rf_predictions)
print("Deep Neural Network Predictions:", dnn_predictions)