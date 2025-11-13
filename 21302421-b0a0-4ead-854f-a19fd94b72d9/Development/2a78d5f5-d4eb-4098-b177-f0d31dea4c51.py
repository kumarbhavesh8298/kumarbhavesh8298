import pandas as pd

# Basic row counts and data overview
total_rows = len(loan_df)
total_cols = len(loan_df.columns)

print("=" * 50)
print("DATASET OVERVIEW")
print("=" * 50)
print(f"Total Rows: {total_rows:,}")
print(f"Total Columns: {total_cols}")
print(f"Memory Usage: {loan_df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
print(f"\nDate Range:")
print(f"  Customer Opening: {loan_df['CUST_OPN_DT'].min()} to {loan_df['CUST_OPN_DT'].max()}")
print(f"  Birth Dates: {loan_df['BRTH_DT'].min()} to {loan_df['BRTH_DT'].max()}")
print(f"  First Disbursement: {loan_df['FIRST_DISBT_DT'].min()} to {loan_df['FIRST_DISBT_DT'].max()}")