import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.api import VAR
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import LSTM, Dense
import json

# Load Brent Oil Prices
file_path = 'C:/Users/user/Desktop/Github/Oilprice_analysis/data/BrentOilPrices.csv'
df = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date', dayfirst=True)

# Check for and handle missing dates
df = df.asfreq('D')
df.fillna(method='ffill', inplace=True)  # Forward fill to handle missing values

# Perform ADF Test for stationarity
adf_result = adfuller(df['Price'].dropna())
results_summary = {
    'ADF Statistic': adf_result[0],
    'p-value': adf_result[1],
}

# Differencing for stationarity
df_diff = df['Price'].diff().dropna()

# EDA: Visualize Oil Prices
plt.figure(figsize=(14, 7))
plt.plot(df['Price'], label='Brent Oil Prices')
plt.title('Historical Brent Oil Prices')
plt.xlabel('Date')
plt.ylabel('Price in USD')
plt.legend()
plt.grid()
plt.show()

# Fit ARIMA Model
def arima_model(df):
    model = ARIMA(df, order=(1, 1, 1))
    results = model.fit()
    return results

# Fit the ARIMA model and save the summary
arima_results = arima_model(df_diff)
results_summary['ARIMA Summary'] = arima_results.summary().as_text()  # Convert summary to text

# Fit VAR Model
# Create a sample DataFrame for illustration (replace this with your actual data).
gdp_data = pd.Series(np.random.randn(len(df)), index=df.index, name='GDP')  # Example GDP data
combined_df = pd.concat([df['Price'], gdp_data], axis=1).dropna()

var_model = VAR(combined_df)
var_results = var_model.fit(maxlags=5)
results_summary['VAR Summary'] = str(var_results.summary())  # Store VAR summary as string

# Save results to a JSON file
with open('C:/Users/user/Desktop/Github/Oilprice_analysis/results.json', 'w') as f:
    json.dump(results_summary, f)

# LSTM Model Implementation
def create_lstm_model(input_shape):
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=input_shape))
    model.add(LSTM(50, return_sequences=False))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Prepare data for LSTM
X = df['Price'].values[:-1].reshape(-1, 1)  # Reshape for LSTM input
y = df['Price'].values[1:]

# Split the dataset into training and testing
train_size = int(len(X) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# Reshape input for LSTM [samples, time steps, features]
X_train = X_train.reshape((X_train.shape[0], 1, X_train.shape[1]))
X_test = X_test.reshape((X_test.shape[0], 1, X_test.shape[1]))

# Create and fit the LSTM model
lstm_model = create_lstm_model((X_train.shape[1], X_train.shape[2]))
lstm_model.fit(X_train, y_train, epochs=50, batch_size=32)

# Predict and calculate performance metrics
predictions = lstm_model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
results_summary['LSTM MSE'] = mse

if __name__ == "__main__":
    # Execute main code if needed
    pass  # Main logic executed above
