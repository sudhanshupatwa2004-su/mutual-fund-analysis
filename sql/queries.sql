-- 1. Top 5 funds by AUM
SELECT scheme_name, fund_house, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per fund
SELECT amfi_code, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;

-- 3. Transaction count by type
SELECT transaction_type, COUNT(*) AS txn_count
FROM fact_transactions
GROUP BY transaction_type;

-- 4. Total investment amount by state
SELECT state, SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY state
ORDER BY total_investment DESC;

-- 5. Funds with expense ratio less than 1%
SELECT scheme_name, fund_house, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6. Average 1-year return by category
SELECT category, AVG(return_1yr_pct) AS avg_return_1yr
FROM fact_performance
GROUP BY category;

-- 7. Average 3-year return by fund house
SELECT fund_house, AVG(return_3yr_pct) AS avg_return_3yr
FROM fact_performance
GROUP BY fund_house
ORDER BY avg_return_3yr DESC;

-- 8. Count of investors by gender
SELECT gender, COUNT(*) AS investor_count
FROM fact_transactions
GROUP BY gender;

-- 9. Count of KYC status
SELECT kyc_status, COUNT(*) AS kyc_count
FROM fact_transactions
GROUP BY kyc_status;

-- 10. Average expense ratio by category
SELECT category, AVG(expense_ratio_pct) AS avg_expense_ratio
FROM fact_performance
GROUP BY category;