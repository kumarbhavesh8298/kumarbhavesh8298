import pandas as pd
import numpy as np

# Calculate loan maturity and payment progress features
# Since we don't have RESIDUAL_TENURE and PRINCIPAL_NO_OF_INSTALL, we'll derive from available data

# 1. Payment progress (what % of payments have been made)
temporal_df['payment_progress_pct'] = (temporal_df['NUM_PAYMENTS_MADE'] / temporal_df['LOAN_TERM']) * 100
temporal_df['payment_progress_pct'] = temporal_df['payment_progress_pct'].clip(0, 100)

# 2. Loan maturity percentage (based on time elapsed)
# Assuming monthly payments, calculate elapsed months from disbursement
_months_elapsed = temporal_df['days_since_disbursement'] / 30.44
temporal_df['loan_maturity_pct'] = (_months_elapsed / temporal_df['LOAN_TERM']) * 100
temporal_df['loan_maturity_pct'] = temporal_df['loan_maturity_pct'].clip(0, 100)

# 3. Remaining tenure percentage (inverse of maturity)
temporal_df['remaining_tenure_pct'] = 100 - temporal_df['loan_maturity_pct']

# 4. Balance depletion rate (how fast is the balance decreasing)
temporal_df['balance_depletion_pct'] = ((temporal_df['FUND_AMT'] - temporal_df['REMAINING_BALANCE']) / temporal_df['FUND_AMT']) * 100
temporal_df['balance_depletion_pct'] = temporal_df['balance_depletion_pct'].clip(0, 100).fillna(0)

# 5. Payment velocity (payments made per year since disbursement)
temporal_df['payment_velocity'] = temporal_df['NUM_PAYMENTS_MADE'] / (temporal_df['loan_age_years'] + 0.01)

# 6. Payment lag indicator (are payments ahead or behind schedule?)
_expected_payments = _months_elapsed.clip(upper=temporal_df['LOAN_TERM'])
temporal_df['payment_lag'] = temporal_df['NUM_PAYMENTS_MADE'] - _expected_payments

print(f'Created 6 loan maturity and progress features')
print(f'Payment progress range: {temporal_df["payment_progress_pct"].min():.1f}% to {temporal_df["payment_progress_pct"].max():.1f}%')
print(f'Loan maturity range: {temporal_df["loan_maturity_pct"].min():.1f}% to {temporal_df["loan_maturity_pct"].max():.1f}%')
print(f'Payment velocity mean: {temporal_df["payment_velocity"].mean():.2f} payments/year')