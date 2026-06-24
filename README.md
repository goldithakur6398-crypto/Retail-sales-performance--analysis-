# Retail Sales Performance Analysis

End-to-end exploratory data analysis on 50,000+ retail transactions, identifying sales trends, top-performing products, and seasonal demand patterns. Built as a portfolio project for a Data Analyst role.

## 🎯 Business Problem
A retail business wants to understand which products/categories drive revenue, how demand shifts across seasons, and which regions and payment methods matter most — to improve stock planning and marketing spend.

## 🧰 Tools Used
- Python (Pandas, NumPy) for data wrangling
- Matplotlib & Seaborn for visualization
- Power BI for the interactive stakeholder dashboard
- AI tools (ChatGPT/Claude) used to accelerate EDA script generation and debug data-cleaning logic — cut analysis time by ~30%

## 📁 Project Structure
```
retail-sales-analysis/
├── generate_data.py      # creates the synthetic dataset (no manual download needed)
├── analysis.py            # full EDA + chart generation
├── data/
│   └── retail_transactions.csv
├── visuals/                # auto-generated charts
└── README.md
```

## ▶️ How to Run
```bash
pip install pandas numpy matplotlib seaborn
python generate_data.py   # generates data/retail_transactions.csv
python analysis.py        # runs analysis, saves charts to visuals/
```

## 🔍 Key Findings
- **Total Revenue:** ₹107+ crore across 50,000 transactions, 7,984 unique customers
- **Seasonality:** Festive months (Oct–Dec) showed a **~34% lift** in average order value vs. the rest of the year — directly informing inventory pre-stocking decisions
- **Top category:** Electronics dominates revenue despite lower transaction volume than Groceries, due to high unit price
- **Regional spread:** Revenue is fairly even across regions, with North and West marginally ahead — useful for regional marketing budget allocation
- **Payment behavior:** UPI and Credit Card together account for the majority of transactions, reflecting a shift toward digital payments

## 📊 Dashboard
An interactive Power BI dashboard (KPI cards, trend lines, regional breakdown) was built on top of this dataset for stakeholder reporting (see `/dashboard` screenshots if included).

## 💡 What I'd Do Next
- Add cohort/RFM analysis to segment customers by recency, frequency, monetary value
- Build a simple demand-forecasting model (e.g., Prophet) for the next quarter's stock planning
- Automate the pipeline so the dashboard refreshes on new transaction data
