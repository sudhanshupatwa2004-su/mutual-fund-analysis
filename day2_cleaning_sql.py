import pandas as pd
import numpy as np

# =========================
# LOAD RAW FILES
# =========================
fund_df = pd.read_csv("data/raw/01_fund_master.csv")
nav_df = pd.read_csv("data/raw/02_nav_history.csv")
aum_df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")
sip_df = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")
cat_df = pd.read_csv("data/raw/05_category_inflows.csv")
folio_df = pd.read_csv("data/raw/06_industry_folio_count.csv")
perf_df = pd.read_csv("data/raw/07_scheme_performance.csv")
txn_df = pd.read_csv("data/raw/08_investor_transactions.csv")
hold_df = pd.read_csv("data/raw/09_portfolio_holdings.csv")
bench_df = pd.read_csv("data/raw/10_benchmark_indices.csv")

# =========================
# CLEAN 01 FUND MASTER
# =========================
fund_df = fund_df.drop_duplicates()

# =========================
# CLEAN 02 NAV HISTORY
# =========================
nav_df["date"] = pd.to_datetime(nav_df["date"], errors="coerce")
nav_df = nav_df.sort_values(["amfi_code", "date"])
nav_df["nav"] = nav_df.groupby("amfi_code")["nav"].ffill()
nav_df = nav_df.drop_duplicates()
nav_df = nav_df[nav_df["nav"] > 0]

# =========================
# CLEAN 03 AUM BY FUND HOUSE
# =========================
aum_df = aum_df.drop_duplicates()

# =========================
# CLEAN 04 MONTHLY SIP INFLOWS
# =========================
sip_df = sip_df.drop_duplicates()

# =========================
# CLEAN 05 CATEGORY INFLOWS
# =========================
cat_df = cat_df.drop_duplicates()

# =========================
# CLEAN 06 INDUSTRY FOLIO COUNT
# =========================
folio_df = folio_df.drop_duplicates()

# =========================
# CLEAN 07 SCHEME PERFORMANCE
# =========================
numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct",
    "morningstar_rating"
]

for col in numeric_cols:
    perf_df[col] = pd.to_numeric(perf_df[col], errors="coerce")

perf_df["expense_ratio_flag"] = np.where(
    (perf_df["expense_ratio_pct"] < 0.1) | (perf_df["expense_ratio_pct"] > 2.5),
    "Check",
    "OK"
)

# =========================
# CLEAN 08 INVESTOR TRANSACTIONS
# =========================
txn_df["transaction_date"] = pd.to_datetime(txn_df["transaction_date"], errors="coerce")
txn_df["transaction_type"] = txn_df["transaction_type"].astype(str).str.strip().str.title()

txn_df["transaction_type"] = txn_df["transaction_type"].replace({
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
})

valid_txn_types = ["SIP", "Lumpsum", "Redemption"]
txn_df = txn_df[txn_df["transaction_type"].isin(valid_txn_types)]
txn_df = txn_df[txn_df["amount_inr"] > 0]
txn_df["kyc_status"] = txn_df["kyc_status"].astype(str).str.strip().str.title()

# =========================
# CLEAN 09 PORTFOLIO HOLDINGS
# =========================
hold_df = hold_df.drop_duplicates()

# =========================
# CLEAN 10 BENCHMARK INDICES
# =========================
bench_df = bench_df.drop_duplicates()

# =========================
# SAVE ALL CLEANED FILES
# =========================
fund_df.to_csv("data/processed/fund_master_cleaned.csv", index=False)
nav_df.to_csv("data/processed/nav_history_cleaned.csv", index=False)
aum_df.to_csv("data/processed/aum_by_fund_house_cleaned.csv", index=False)
sip_df.to_csv("data/processed/monthly_sip_inflows_cleaned.csv", index=False)
cat_df.to_csv("data/processed/category_inflows_cleaned.csv", index=False)
folio_df.to_csv("data/processed/industry_folio_count_cleaned.csv", index=False)
perf_df.to_csv("data/processed/scheme_performance_cleaned.csv", index=False)
txn_df.to_csv("data/processed/investor_transactions_cleaned.csv", index=False)
hold_df.to_csv("data/processed/portfolio_holdings_cleaned.csv", index=False)
bench_df.to_csv("data/processed/benchmark_indices_cleaned.csv", index=False)

print("All 10 cleaned files saved successfully in data/processed/")