import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the sales data
data = pd.read_csv('sales_data.csv')

# Data summary
print("Data Preview:")
print(data.head())

# Handle missing values
data = data.dropna()  # Remove rows with missing values
print("\nCleaned Data:")
print(data.info())

# Group data by region
regional_sales = data.groupby('Region')['Sales Amount'].sum().reset_index()

# Identify trends and outliers
sales_mean = np.mean(data['Sales Amount'])
sales_std = np.std(data['Sales Amount'])
outliers = data[data['Sales Amount'] > sales_mean + 2 * sales_std]

# Visualize regional sales
plt.bar(regional_sales['Region'], regional_sales['Sales Amount'], color='blue')
plt.title('Regional Sales Performance')
plt.xlabel('Region')
plt.ylabel('Total Sales Amount')
plt.show()

# Display insights
print("\nSales Insights:")
print(f"Average Sales: {sales_mean}")
print(f"Outliers:\n{outliers}")
