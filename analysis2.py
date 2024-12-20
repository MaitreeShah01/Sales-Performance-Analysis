import pandas as pd
import numpy as np
from faker import Faker
import random
import matplotlib.pyplot as plt
import seaborn as sns

FAKE = Faker() # Initialize Faker

random.seed(42)   # Set random seed for reproducibility
np.random.seed(42)

num_rec = 1000    # Generate synthetic sales data

# Define values
Region = ['North', 'South', 'East', 'West']
Products = ['Product A', 'Product B', 'Product C', 'Product D']
salesperson = [FAKE.name() for _ in range(50)]

# DataFrame Created
sales_data = pd.DataFrame({
    'Transaction_ID': [FAKE.uuid4() for _ in range(num_rec)],
    'Date': [FAKE.date_between(start_date='-2y', end_date='today') for _ in range(num_rec)],
    'Region': [random.choice(Region) for _ in range(num_rec)],
    'Product': [random.choice(Products) for _ in range(num_rec)],
    'Salesperson': [random.choice(salesperson) for _ in range(num_rec)],
    'Units_Sold': np.random.randint(1, 50, num_rec),
    'Unit_Price': np.random.uniform(10, 500, num_rec).round(2),
})

sales_data['Total_Sales'] = (sales_data['Units_Sold'] * sales_data['Unit_Price']).round(2)    # Calculate Total_Sales

# Save file into CSV
output_path = "sales_data.csv"
sales_data.to_csv(output_path, index=False)
print(f"Sales data saved to {output_path}")

sales_data = pd.read_csv(output_path)    # Load the generated sales data
sales_data['Date'] = pd.to_datetime(sales_data['Date'])   # Convert 'Date' column to datetime
sales_trend = sales_data.resample('M', on='Date')['Total_Sales'].sum()    # Exploratory Data Analysis using Group data by month for trend analysis

# Ploting the sales trend
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.lineplot(x=sales_trend.index, y=sales_trend.values, marker='o', color='blue')
plt.title('Monthly Sales Trend', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_trend.png")
print("Monthly Sales Trend plot saved as sales_trend.png")

# Analyze Top sales Performers
TopRegion = sales_data.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)
TopProducts = sales_data.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)
Topsalesperson = sales_data.groupby('Salesperson')['Total_Sales'].sum().sort_values(ascending=False)

# Save results to CSV
TopRegion.to_csv("top_regions.csv", header=['Total_Sales'])
TopProducts.to_csv("top_products.csv", header=['Total_Sales'])
Topsalesperson.to_csv("top_salespeople.csv", header=['Total_Sales'])
print("Top performers saved to CSV files.")

# Transfering analysied data to Tableau
processed_data_path = "processed_sales_data.csv"
sales_data.to_csv(processed_data_path, index=False)
print(f"Processed sales data exported for Tableau: {processed_data_path}")
