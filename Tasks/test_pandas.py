import pandas as pd

# Using forward slashes
file_path = 'C:/Users/Admin/Python-files/Documents/HR_Analytics.csv'

# Reading the CSV file
try:
    data = pd.read_csv(file_path)
    # Display the entire DataFrame
    print(data.to_string())
except FileNotFoundError as e:
    print(f"Error: {e}")

print(data.shape)
print(data.dtypes)
print(data.head())
print(data.head(20))
print(data.tail())
print(data.tail(15))
print(data.describe())
print(data.info())
print(data.isnull())
