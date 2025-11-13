import pandas as pd
import matplotlib.pyplot as plt

# Create comprehensive summary statistics table
print('='*80)
print('COMPREHENSIVE SUMMARY STATISTICS TABLE')
print('='*80)
print(f'\nDataFrame Shape: {loan_df.shape}')
print(f'Total Rows: {len(loan_df)}')
print(f'Total Columns: {len(loan_df.columns)}')

# Display formatted distribution stats
print('\n' + '='*80)
print('DISTRIBUTION STATISTICS (Skewness & Kurtosis)')
print('='*80)
print(distribution_stats_df.to_string(index=False))

# Key financial metrics summary
key_financial = ["FUND_AMT", "BALANCE", "TOTAL_ASSETS", "ANNUAL_INCOME", "CREDIT_SCORE"]
print('\n' + '='*80)
print('KEY FINANCIAL METRICS - DETAILED STATISTICS')
print('='*80)
financial_summary = loan_df[key_financial].describe()
print(financial_summary.to_string())

# Categorical distribution summary
categorical_features = [
    "MARITAL_STATUS", "INDUSTRY_SECTOR", "LOAN_STATUS", 
    "EMPLOYMENT_STATUS", "REGION"
]

print('\n' + '='*80)
print('CATEGORICAL FEATURE DISTRIBUTIONS')
print('='*80)
for _cat_feat in categorical_features:
    print(f'\n{_cat_feat}:')
    _value_distribution = loan_df[_cat_feat].value_counts()
    for _cat_val, _cat_count in _value_distribution.items():
        _percentage = (_cat_count / len(loan_df)) * 100
        print(f'  {_cat_val}: {_cat_count} ({_percentage:.1f}%)')

print('\n' + '='*80)
print('SUMMARY COMPLETE')
print('='*80)