import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller

# Load data
file_path = 'C:/Users/user/Desktop/Github/Oilprice_analysis/data/BrentOilPrices.csv'
df = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')

# Check for and handle missing dates
df = df.asfreq('D')  # Fill missing dates with NaN, or use 'B' for business days

# Print DataFrame columns to check names
print("Columns in the DataFrame:", df.columns)

# Perform ADF Test for stationarity
adf_result = adfuller(df['Price'].dropna())  # Ensure NaNs are dropped for the test
print(f'ADF Statistic: {adf_result[0]}')
print(f'p-value: {adf_result[1]}')

# Differencing the data for stationarity
df_diff = df['Price'].diff().dropna()

# ARIMA Model
def arima_model(df):
    # Fit an ARIMA model; you can adjust the order as needed
    model = ARIMA(df, order=(1, 1, 1))  # Example: ARIMA(1,1,1)
    results = model.fit()
    return results

# Main function to run analysis
def main():
    results = arima_model(df_diff)
    print(results.summary())

if __name__ == "__main__":
    main()
