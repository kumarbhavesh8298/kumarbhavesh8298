import pandas as pd
import numpy as np

# Calculate temporal age features from date columns
# We'll use a reference date for calculating ages (typically today's date, but we'll use the max date from the data)
reference_date = pd.Timestamp('2024-01-01')

# Create dataframe with temporal features
temporal_df = imputed_df.copy()

# 1. Customer Age (from BRTH_DT)
temporal_df['customer_age_years'] = (reference_date - temporal_df['BRTH_DT']).dt.days / 365.25

# 2. Account Age (from CUST_OPN_DT)
temporal_df['account_age_years'] = (reference_date - temporal_df['CUST_OPN_DT']).dt.days / 365.25

# 3. Loan Age (from FIRST_DISBT_DT)
temporal_df['loan_age_years'] = (reference_date - temporal_df['FIRST_DISBT_DT']).dt.days / 365.25

# 4. Days since disbursement
temporal_df['days_since_disbursement'] = (reference_date - temporal_df['FIRST_DISBT_DT']).dt.days

# 5. Days since last payment
temporal_df['days_since_last_payment'] = (reference_date - temporal_df['LAST_PAYMENT_DATE']).dt.days

# 6. Days until next payment
temporal_df['days_until_next_payment'] = (temporal_df['NEXT_PAYMENT_DATE'] - reference_date).dt.days

print(f'Created 6 temporal age features based on date calculations')
print(f'Reference date: {reference_date}')
print(f'Customer age range: {temporal_df["customer_age_years"].min():.1f} to {temporal_df["customer_age_years"].max():.1f} years')
print(f'Account age range: {temporal_df["account_age_years"].min():.1f} to {temporal_df["account_age_years"].max():.1f} years')
print(f'Loan age range: {temporal_df["loan_age_years"].min():.1f} to {temporal_df["loan_age_years"].max():.1f} years')