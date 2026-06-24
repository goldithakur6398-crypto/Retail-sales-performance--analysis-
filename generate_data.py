"""
generate_data.py
-----------------
Creates a realistic synthetic retail transactions dataset so the project
runs end-to-end with zero manual downloads.

Run this first:
    python generate_data.py
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta

np.random.seed(42)

N_ROWS = 50000

categories = {
    "Electronics": ["Headphones", "Smartphone", "Laptop", "Smartwatch", "Tablet"],
    "Clothing": ["T-Shirt", "Jeans", "Jacket", "Sneakers", "Cap"],
    "Home & Kitchen": ["Mixer", "Cookware Set", "Vacuum Cleaner", "Lamp", "Bedsheet"],
    "Groceries": ["Rice 5kg", "Cooking Oil", "Snack Pack", "Tea Box", "Spices Combo"],
    "Beauty": ["Face Wash", "Shampoo", "Perfume", "Lipstick", "Sunscreen"],
}

regions = ["North", "South", "East", "West", "Central"]
payment_modes = ["Credit Card", "Debit Card", "UPI", "Cash", "Net Banking"]

start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 12, 31)
date_range_days = (end_date - start_date).days

rows = []
for i in range(1, N_ROWS + 1):
    category = np.random.choice(list(categories.keys()), p=[0.25, 0.25, 0.2, 0.2, 0.1])
    product = np.random.choice(categories[category])

    # seasonal bump: more sales in Oct-Dec (festive/holiday season)
    day_offset = np.random.randint(0, date_range_days)
    txn_date = start_date + timedelta(days=day_offset)
    seasonal_boost = 1.6 if txn_date.month in [10, 11, 12] else 1.0

    base_price = {
        "Electronics": np.random.uniform(800, 60000),
        "Clothing": np.random.uniform(300, 4000),
        "Home & Kitchen": np.random.uniform(500, 12000),
        "Groceries": np.random.uniform(50, 1500),
        "Beauty": np.random.uniform(100, 2500),
    }[category]

    quantity = max(1, int(np.random.poisson(2) * seasonal_boost))
    unit_price = round(base_price, 2)
    discount_pct = np.random.choice([0, 5, 10, 15, 20], p=[0.4, 0.25, 0.2, 0.1, 0.05])
    gross_amount = unit_price * quantity
    discount_amount = round(gross_amount * discount_pct / 100, 2)
    net_amount = round(gross_amount - discount_amount, 2)

    rows.append({
        "transaction_id": f"TXN{i:06d}",
        "transaction_date": txn_date.strftime("%Y-%m-%d"),
        "customer_id": f"CUST{np.random.randint(1, 8000):05d}",
        "region": np.random.choice(regions),
        "category": category,
        "product": product,
        "quantity": quantity,
        "unit_price": unit_price,
        "discount_pct": discount_pct,
        "gross_amount": round(gross_amount, 2),
        "discount_amount": discount_amount,
        "net_amount": net_amount,
        "payment_mode": np.random.choice(payment_modes),
    })

df = pd.DataFrame(rows)
df.to_csv("data/retail_transactions.csv", index=False)
print(f"Generated {len(df)} rows -> data/retail_transactions.csv")
print(df.head())
