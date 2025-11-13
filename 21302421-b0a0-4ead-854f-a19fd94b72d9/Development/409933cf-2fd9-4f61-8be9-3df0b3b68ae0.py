import pandas as pd
import numpy as np

# Extract cyclical temporal patterns from date fields
# Year, month, quarter, day of week, day of year for seasonality analysis

# From CUST_OPN_DT (account opening date)
temporal_df['account_open_year'] = temporal_df['CUST_OPN_DT'].dt.year
temporal_df['account_open_month'] = temporal_df['CUST_OPN_DT'].dt.month
temporal_df['account_open_quarter'] = temporal_df['CUST_OPN_DT'].dt.quarter
temporal_df['account_open_dayofweek'] = temporal_df['CUST_OPN_DT'].dt.dayofweek

# From FIRST_DISBT_DT (loan disbursement date)
temporal_df['loan_disb_year'] = temporal_df['FIRST_DISBT_DT'].dt.year
temporal_df['loan_disb_month'] = temporal_df['FIRST_DISBT_DT'].dt.month
temporal_df['loan_disb_quarter'] = temporal_df['FIRST_DISBT_DT'].dt.quarter
temporal_df['loan_disb_dayofweek'] = temporal_df['FIRST_DISBT_DT'].dt.dayofweek

# From BRTH_DT (birth date)
temporal_df['birth_year'] = temporal_df['BRTH_DT'].dt.year
temporal_df['birth_month'] = temporal_df['BRTH_DT'].dt.month

# From LAST_PAYMENT_DATE
temporal_df['last_payment_year'] = temporal_df['LAST_PAYMENT_DATE'].dt.year
temporal_df['last_payment_month'] = temporal_df['LAST_PAYMENT_DATE'].dt.month
temporal_df['last_payment_quarter'] = temporal_df['LAST_PAYMENT_DATE'].dt.quarter

print(f'Created 13 cyclical temporal pattern features')
print(f'Date components extracted from CUST_OPN_DT, FIRST_DISBT_DT, BRTH_DT, LAST_PAYMENT_DATE')
print(f'Account open years: {temporal_df["account_open_year"].min()} to {temporal_df["account_open_year"].max()}')
print(f'Loan disbursement years: {temporal_df["loan_disb_year"].min()} to {temporal_df["loan_disb_year"].max()}')