"""
analysis.py
------------
Retail Sales Performance Analysis
Run after generate_data.py:
    python analysis.py
Outputs charts to visuals/ and prints key insights to console.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# ---------- 1. Load & Clean ----------
df = pd.read_csv("data/retail_transactions.csv", parse_dates=["transaction_date"])

print("Shape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicates:", df.duplicated().sum())

df["month"] = df["transaction_date"].dt.to_period("M")
df["month_name"] = df["transaction_date"].dt.strftime("%b %Y")
df["year"] = df["transaction_date"].dt.year

# ---------- 2. Top-performing products ----------
top_products = (
    df.groupby("product")["net_amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print("\nTop 10 products by revenue:\n", top_products)

plt.figure()
sns.barplot(x=top_products.values, y=top_products.index, palette="viridis")
plt.title("Top 10 Products by Revenue")
plt.xlabel("Net Revenue (₹)")
plt.tight_layout()
plt.savefig("visuals/top_products.png", dpi=150)
plt.close()

# ---------- 3. Category performance ----------
category_rev = df.groupby("category")["net_amount"].sum().sort_values(ascending=False)

plt.figure()
sns.barplot(x=category_rev.index, y=category_rev.values, palette="magma")
plt.title("Revenue by Category")
plt.ylabel("Net Revenue (₹)")
plt.tight_layout()
plt.savefig("visuals/category_revenue.png", dpi=150)
plt.close()

# ---------- 4. Seasonal demand pattern ----------
monthly_sales = df.groupby("month")["net_amount"].sum()

plt.figure()
monthly_sales.plot(kind="line", marker="o", color="steelblue")
plt.title("Monthly Sales Trend (Seasonality Check)")
plt.ylabel("Net Revenue (₹)")
plt.xlabel("Month")
plt.tight_layout()
plt.savefig("visuals/monthly_trend.png", dpi=150)
plt.close()

festive_months = df[df["transaction_date"].dt.month.isin([10, 11, 12])]
non_festive_months = df[~df["transaction_date"].dt.month.isin([10, 11, 12])]
festive_avg = festive_months["net_amount"].mean()
non_festive_avg = non_festive_months["net_amount"].mean()
seasonal_lift_pct = round(((festive_avg - non_festive_avg) / non_festive_avg) * 100, 2)
print(f"\nFestive season (Oct-Dec) average order value lift: {seasonal_lift_pct}%")

# ---------- 5. Regional breakdown ----------
region_rev = df.groupby("region")["net_amount"].sum().sort_values(ascending=False)

plt.figure()
sns.barplot(x=region_rev.index, y=region_rev.values, palette="crest")
plt.title("Revenue by Region")
plt.ylabel("Net Revenue (₹)")
plt.tight_layout()
plt.savefig("visuals/region_revenue.png", dpi=150)
plt.close()

# ---------- 6. Payment mode mix ----------
payment_mix = df["payment_mode"].value_counts()

plt.figure()
plt.pie(payment_mix.values, labels=payment_mix.index, autopct="%1.1f%%", startangle=90)
plt.title("Payment Mode Distribution")
plt.tight_layout()
plt.savefig("visuals/payment_mode.png", dpi=150)
plt.close()

# ---------- 7. KPI summary ----------
total_revenue = df["net_amount"].sum()
total_orders = df["transaction_id"].nunique()
avg_order_value = round(df["net_amount"].mean(), 2)
total_customers = df["customer_id"].nunique()

print("\n--- KPI SUMMARY ---")
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Avg Order Value: ₹{avg_order_value:,.2f}")
print(f"Unique Customers: {total_customers:,}")

print("\nAll charts saved to visuals/ folder.")
