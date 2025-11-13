import pandas as pd

# Profile numeric/financial fields - ranges and statistics
numeric_financial_cols = [
    'FUND_AMT', 'BALANCE', 'TOTAL_ASSETS', 'TOTAL_LIABILITIES',
    'ANNUAL_INCOME', 'CREDIT_SCORE', 'INTEREST_RATE', 'COLLATERAL_VALUE',
    'BUSINESS_REVENUE', 'BUSINESS_EXPENSES', 'NET_PROFIT', 'CASH_FLOW', 
    'OPERATING_PROFIT'
]

print("=" * 50)
print("NUMERIC/FINANCIAL FIELDS PROFILE")
print("=" * 50)

for num_col in numeric_financial_cols:
    col_min = loan_df[num_col].min()
    col_max = loan_df[num_col].max()
    col_mean = loan_df[num_col].mean()
    col_median = loan_df[num_col].median()
    
    print(f"\n{num_col}:")
    print(f"  Range: {col_min:,.2f} to {col_max:,.2f}")
    print(f"  Mean: {col_mean:,.2f} | Median: {col_median:,.2f}")