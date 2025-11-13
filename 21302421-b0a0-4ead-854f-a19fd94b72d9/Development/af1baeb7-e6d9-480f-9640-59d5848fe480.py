import pandas as pd
import numpy as np

# Identify data quality issues and patterns
print('='*80)
print('DATA QUALITY ASSESSMENT')
print('='*80)

# Check for missing values
print('\n1. MISSING VALUES:')
missing_vals = loan_df.isnull().sum()
if missing_vals.sum() == 0:
    print('   ✓ No missing values detected')
else:
    print(f'   Columns with missing values:')
    for _col_miss, _count_miss in missing_vals[missing_vals > 0].items():
        print(f'   - {_col_miss}: {_count_miss} ({(_count_miss/len(loan_df)*100):.1f}%)')

# Check for outliers using IQR method
print('\n2. OUTLIER DETECTION (IQR Method):')
outlier_summary = []

numeric_features = [
    "FUND_AMT", "BALANCE", "TOTAL_ASSETS", "ANNUAL_INCOME",
    "BUSINESS_REVENUE", "NET_PROFIT", "CREDIT_SCORE"
]

for _feat in numeric_features:
    _q1_out = loan_df[_feat].quantile(0.25)
    _q3_out = loan_df[_feat].quantile(0.75)
    _iqr_out = _q3_out - _q1_out
    _lower_bound = _q1_out - 1.5 * _iqr_out
    _upper_bound = _q3_out + 1.5 * _iqr_out
    
    _outliers_mask = (loan_df[_feat] < _lower_bound) | (loan_df[_feat] > _upper_bound)
    _outlier_count = _outliers_mask.sum()
    _outlier_pct = (_outlier_count / len(loan_df)) * 100
    
    if _outlier_count > 0:
        outlier_summary.append({
            'Feature': _feat,
            'Outlier_Count': _outlier_count,
            'Outlier_Percentage': _outlier_pct
        })

if outlier_summary:
    for _item in outlier_summary:
        print(f"   - {_item['Feature']}: {_item['Outlier_Count']} outliers ({_item['Outlier_Percentage']:.1f}%)")
else:
    print('   ✓ No significant outliers detected')

# Check for negative values in features that should be positive
print('\n3. NEGATIVE VALUES CHECK:')
positive_only_cols = ["FUND_AMT", "BALANCE", "TOTAL_ASSETS", "ANNUAL_INCOME", "CREDIT_SCORE"]
negative_issues = []

for _pos_col in positive_only_cols:
    _neg_count = (loan_df[_pos_col] < 0).sum()
    if _neg_count > 0:
        negative_issues.append(f'{_pos_col}: {_neg_count} negative values')

if negative_issues:
    for _issue in negative_issues:
        print(f'   ⚠ {_issue}')
else:
    print('   ✓ No unexpected negative values')

# Distribution balance check
print('\n4. CLASS BALANCE (Categorical Features):')
for _cat_check in ["LOAN_STATUS", "MARITAL_STATUS", "EMPLOYMENT_STATUS"]:
    _value_counts_check = loan_df[_cat_check].value_counts()
    _max_pct = (_value_counts_check.max() / len(loan_df)) * 100
    _min_pct = (_value_counts_check.min() / len(loan_df)) * 100
    _balance_ratio = _max_pct / _min_pct
    
    if _balance_ratio > 2:
        print(f'   ⚠ {_cat_check}: Imbalanced (max: {_max_pct:.1f}%, min: {_min_pct:.1f}%)')
    else:
        print(f'   ✓ {_cat_check}: Well-balanced')

print('\n' + '='*80)
print('QUALITY ASSESSMENT COMPLETE')
print('='*80)