import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('sales_data.csv')

# Display the first few rows of the dataset
print("Dataset Preview:")
print(data.head())

# Display dataset information
print("\nDataset Information:")
print(data.info())

# Display summary statistics
print("\nSummary Statistics:")
print(data.describe())

# Total sales by region
print("\nTotal Sales by Region:")
regional_sales = data.groupby('Region')['Sales Amount'].sum()
print(regional_sales)

# Monthly sales trend (assuming the dataset has enough data for trends)
data['Date'] = pd.to_datetime(data['Date'])  # Convert Date column to datetime
monthly_sales = data.groupby(data['Date'].dt.to_period('M'))['Sales Amount'].sum()

print("\nMonthly Sales Trend:")
print(monthly_sales)

# Visualize total sales by region
plt.figure(figsize=(8, 5))
regional_sales.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Region', fontsize=14)
plt.xlabel('Region', fontsize=12)
plt.ylabel('Sales Amount', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('regional_sales.png')  # Save plot as an image
plt.show()

# Visualize monthly sales trend
plt.figure(figsize=(8, 5))
monthly_sales.plot(kind='line', marker='o', color='green')
plt.title('Monthly Sales Trend', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales Amount', fontsize=12)
plt.grid()
plt.tight_layout()
plt.savefig('monthly_sales_trend.png')  # Save plot as an image
plt.show()

# Identify outliers using standard deviation
sales_mean = data['Sales Amount'].mean()
sales_std = data['Sales Amount'].std()
upper_limit = sales_mean + 3 * sales_std
lower_limit = sales_mean - 3 * sales_std

outliers = data[(data['Sales Amount'] > upper_limit) | (data['Sales Amount'] < lower_limit)]
print("\nIdentified Outliers:")
print(outliers)
