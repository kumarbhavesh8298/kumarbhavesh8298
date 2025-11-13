import pandas as pd
import numpy as np
from scipy import stats

# Analyze skewness and kurtosis for all numeric columns
all_numeric_cols = [
    "FUND_AMT", "BALANCE", "TOTAL_ASSETS", "TOTAL_LIABILITIES",
    "ANNUAL_INCOME", "CREDIT_SCORE", "INTEREST_RATE", "COLLATERAL_VALUE",
    "BUSINESS_REVENUE", "BUSINESS_EXPENSES", "NET_PROFIT",
    "CASH_FLOW", "OPERATING_PROFIT", "LOAN_TERM", "YEARS_EMPLOYED",
    "DEBT_TO_INCOME", "NUM_DEPENDENTS", "CREDIT_HISTORY_LENGTH",
    "NUM_CREDIT_ACCOUNTS", "CREDIT_UTILIZATION", "NUM_RECENT_INQUIRIES",
    "PAYMENT_HISTORY_SCORE", "DAYS_PAST_DUE", "NUM_PAYMENTS_MADE",
    "TOTAL_PAID", "REMAINING_BALANCE"
]

dist_analysis_results = []

for _col_name in all_numeric_cols:
    _col_data = loan_df[_col_name].dropna()
    
    _skew = stats.skew(_col_data)
    _kurt = stats.kurtosis(_col_data)
    _mean = _col_data.mean()
    _std = _col_data.std()
    
    # Classify distribution type based on skewness
    if abs(_skew) < 0.5:
        _dist_type = 'Symmetric'
    elif _skew > 0:
        _dist_type = 'Right-skewed'
    else:
        _dist_type = 'Left-skewed'
    
    dist_analysis_results.append({
        'Feature': _col_name,
        'Mean': _mean,
        'Std': _std,
        'Skewness': _skew,
        'Kurtosis': _kurt,
        'Distribution_Type': _dist_type
    })

distribution_stats_df = pd.DataFrame(dist_analysis_results)

print('Distribution Analysis Summary:')
print(f'Total features analyzed: {len(distribution_stats_df)}')
print(f"\nDistribution types:")
print(distribution_stats_df['Distribution_Type'].value_counts())
print(f"\nFeatures with high skewness (|skew| > 1):")
print(distribution_stats_df[abs(distribution_stats_df['Skewness']) > 1]['Feature'].tolist())