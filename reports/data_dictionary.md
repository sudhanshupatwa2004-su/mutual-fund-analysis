# Data Dictionary

## 1. dim_fund / fund_master
| Column Name | Data Type | Description |
|------------|-----------|-------------|
| amfi_code | TEXT | Unique AMFI scheme code |
| fund_house | TEXT | Name of fund house / AMC |
| scheme_name | TEXT | Name of mutual fund scheme |
| category | TEXT | Main category of the scheme |
| sub_category | TEXT | Sub-category of the scheme |
| plan | TEXT | Direct / Regular plan |
| launch_date | TEXT | Date when the scheme was launched |
| benchmark | TEXT | Benchmark index for comparison |
| expense_ratio_pct | REAL | Expense ratio in percentage |
| exit_load_pct | REAL | Exit load percentage |
| fund_manager | TEXT | Name of fund manager |
| risk_category | TEXT | Risk classification of the scheme |
| sebi_category_code | TEXT | SEBI category code |

## 2. fact_nav / nav_history_cleaned
| Column Name | Data Type | Description |
|------------|-----------|-------------|
| amfi_code | TEXT | AMFI scheme code |
| date | TEXT | NAV date |
| nav | REAL | Net Asset Value of the fund |

## 3. fact_transactions / investor_transactions_cleaned
| Column Name | Data Type | Description |
|------------|-----------|-------------|
| investor_id | TEXT | Unique investor identifier |
| transaction_date | TEXT | Date of transaction |
| amfi_code | TEXT | AMFI scheme code |
| transaction_type | TEXT | Type of transaction (SIP, Lumpsum, Redemption) |
| amount_inr | REAL | Transaction amount in INR |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| city_tier | TEXT | City tier classification |
| age_group | TEXT | Investor age group |
| gender | TEXT | Investor gender |
| annual_income_lakh | REAL | Annual income in lakhs |
| payment_mode | TEXT | Mode of payment |
| kyc_status | TEXT | KYC completion status |

## 4. fact_performance / scheme_performance_cleaned
| Column Name | Data Type | Description |
|------------|-----------|-------------|
| amfi_code | TEXT | AMFI scheme code |
| scheme_name | TEXT | Name of the mutual fund scheme |
| fund_house | TEXT | Name of fund house |
| category | TEXT | Scheme category |
| plan | TEXT | Direct / Regular plan |
| return_1yr_pct | REAL | 1-year return percentage |
| return_3yr_pct | REAL | 3-year return percentage |
| return_5yr_pct | REAL | 5-year return percentage |
| benchmark_3yr_pct | REAL | 3-year benchmark return percentage |
| alpha | REAL | Alpha of the fund |
| beta | REAL | Beta of the fund |
| sharpe_ratio | REAL | Sharpe ratio |
| sortino_ratio | REAL | Sortino ratio |
| std_dev_ann_pct | REAL | Annualized standard deviation |
| max_drawdown_pct | REAL | Maximum drawdown percentage |
| aum_crore | REAL | Assets under management in crores |
| expense_ratio_pct | REAL | Expense ratio percentage |
| morningstar_rating | REAL | Morningstar rating |
| risk_grade | TEXT | Risk grade of the fund |