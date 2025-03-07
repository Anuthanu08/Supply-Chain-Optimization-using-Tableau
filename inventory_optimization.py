import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load Data
df = pd.read_csv("../data/cleaned_inventory_sales.csv")

# Define Features & Target
X = df[['units_sold', 'stock_level']]
y = df['reorder_level']

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict Reorder Levels
df['predicted_reorder'] = model.predict(X)

# Economic Order Quantity (EOQ)
D = df['units_sold'].mean() * 12  # Annual demand
S = 50  # Ordering cost per order
H = 5   # Holding cost per unit per year
df['EOQ'] = np.sqrt((2 * D * S) / H)

# Save Results
df.to_csv("../data/optimized_inventory.csv", index=False)
