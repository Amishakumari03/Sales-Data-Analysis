import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

# Data Cleaning
df = df.dropna()
df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'])
df['Price Each'] = pd.to_numeric(df['Price Each'])

# Feature Engineering
df['Sales'] = df['Quantity Ordered'] * df['Price Each']
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.month

# Monthly Sales
monthly_sales = df.groupby('Month')['Sales'].sum()
print("Monthly Sales:\n", monthly_sales)

# Product Sales
product_sales = df.groupby('Product')['Quantity Ordered'].sum()
print("\nProduct Sales:\n", product_sales)

# City Extraction
df['City'] = df['Purchase Address'].apply(lambda x: x.split(",")[1])
city_sales = df.groupby('City')['Sales'].sum()
print("\nCity Sales:\n", city_sales)

# Plot
monthly_sales.plot(kind='bar', title='Monthly Sales')
plt.show()
