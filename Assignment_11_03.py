import pandas as pd

# Sample data
asking_prices = pd.Series([10000, 12000, 9000, 15000, 11000])
fair_prices = pd.Series([10500, 11500, 9500, 15000, 13000])

# Find indices where asking_price < fair_price
good_deals = asking_prices < fair_prices

# Get the indices as a list
good_deal_indices = good_deals[good_deals].index.tolist()

print("Indices of good deals:", good_deal_indices)
