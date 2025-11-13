import pandas as pd
import numpy as np

# Introduce realistic missing data patterns for analysis
# This simulates real-world scenarios where data may be missing
np.random.seed(42)

loan_df_with_missing = loan_df.copy()

# MCAR pattern: Random missing (~5-10%)
mcar_cols = ['CREDIT_SCORE', 'ANNUAL_INCOME', 'YEARS_EMPLOYED']
for _col in mcar_cols:
    _mask = np.random.random(len(loan_df_with_missing)) < 0.08
    loan_df_with_missing.loc[_mask, _col] = np.nan

# MAR pattern: Missing depends on other variables (~15-25%)
# Business fields missing for non-business loans
_business_mask = loan_df_with_missing['LOAN_PURPOSE'] != 'BUSINESS'
mar_business_cols = ['BUSINESS_REVENUE', 'BUSINESS_EXPENSES', 'NET_PROFIT', 'CASH_FLOW', 'OPERATING_PROFIT']
for _col in mar_business_cols:
    loan_df_with_missing.loc[_business_mask, _col] = np.nan

# Collateral missing for personal/education loans
_no_collateral = loan_df_with_missing['LOAN_PURPOSE'].isin(['PERSONAL', 'EDUCATION'])
loan_df_with_missing.loc[_no_collateral, 'COLLATERAL_VALUE'] = np.nan

# MNAR pattern: High earners less likely to report debt (~10-15%)
_high_income = loan_df_with_missing['ANNUAL_INCOME'] > 200000
_debt_missing = np.random.random(len(loan_df_with_missing)) < 0.45
loan_df_with_missing.loc[_high_income & _debt_missing, 'DEBT_TO_INCOME'] = np.nan

# Calculate missing data percentages
missing_counts = loan_df_with_missing.isnull().sum()
missing_percentages = (missing_counts / len(loan_df_with_missing)) * 100

# Create summary dataframe sorted by missingness
missing_summary_df = pd.DataFrame({
    'feature': missing_counts.index,
    'missing_count': missing_counts.values,
    'missing_pct': missing_percentages.values
}).sort_values('missing_pct', ascending=False)

# Identify high missingness features (>40%)
high_miss_features = missing_summary_df[missing_summary_df['missing_pct'] > 40]['feature'].tolist()

print(f'Missing data introduced and calculated for {len(loan_df_with_missing.columns)} features')
print(f'Features with >40% missing: {len(high_miss_features)}')
print(f'Total features with any missing data: {(missing_summary_df["missing_pct"] > 0).sum()}')