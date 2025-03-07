import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Load Cleaned Data
df = pd.read_csv("../data/cleaned_inventory_sales.csv")
df['month'] = pd.to_datetime(df['month'])

# Filter for a specific product
product_sales = df[df['product_id'] == 'P001'].set_index('month')

# ARIMA Model
model = ARIMA(product_sales['units_sold'], order=(5,1,0))
model_fit = model.fit()
forecast = model_fit.forecast(steps=6)  # Forecast next 6 months

# Plot Forecast
plt.plot(product_sales['units_sold'], label="Actual Sales")
plt.plot(forecast, label="Forecast", linestyle="dashed")
plt.legend()
plt.show()
