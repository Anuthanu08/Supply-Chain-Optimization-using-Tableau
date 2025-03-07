import pandas as pd

# Load Data
inventory = pd.read_csv("../data/inventory_data.csv")
sales = pd.read_csv("../data/sales_data.csv")

# Merge Datasets
df = pd.merge(inventory, sales, on="product_id", how="left")

# Handle Missing Values
df.fillna(method='ffill', inplace=True)

# Convert Date Column
df['sales_date'] = pd.to_datetime(df['sales_date'])
df['month'] = df['sales_date'].dt.to_period('M')

# Aggregate Sales by Month
monthly_sales = df.groupby(['product_id', 'month'])['units_sold'].sum().reset_index()

# Save Cleaned Data
df.to_csv("../data/cleaned_inventory_sales.csv", index=False)
