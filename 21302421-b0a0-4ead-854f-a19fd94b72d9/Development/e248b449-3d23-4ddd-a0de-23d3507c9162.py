import pandas as pd
import numpy as np

# Create comprehensive imputation metadata report
# This includes strategy used, values imputed, and flags for each feature

imputation_metadata = []

# Forward-fill features
ffill_features = ['DEBT_TO_INCOME', 'YEARS_EMPLOYED']
for feat in ffill_features:
    imputation_metadata.append({
        'feature': feat,
        'strategy': 'Forward-Fill (Time-Series)',
        'values_imputed': loan_df_with_missing[feat].isnull().sum(),
        'flag_column': f'{feat}_imputed_ffill'
    })

# Median imputation features
median_features = ['COLLATERAL_VALUE']
for feat in median_features:
    imputation_metadata.append({
        'feature': feat,
        'strategy': 'Median (Financial Feature)',
        'values_imputed': loan_df_with_missing[feat].isnull().sum(),
        'flag_column': f'{feat}_imputed_median'
    })

# KNN imputation features
knn_features_list = ['CREDIT_SCORE', 'ANNUAL_INCOME']
for feat in knn_features_list:
    imputation_metadata.append({
        'feature': feat,
        'strategy': 'KNN (k=5, Correlated Financial)',
        'values_imputed': loan_df_with_missing[feat].isnull().sum(),
        'flag_column': f'{feat}_imputed_knn'
    })

# Domain-specific business features
business_features_list = mar_business_cols
for feat in business_features_list:
    imputation_metadata.append({
        'feature': feat,
        'strategy': 'Domain Rule (Non-Business = 0)',
        'values_imputed': loan_df_with_missing[feat].isnull().sum(),
        'flag_column': f'{feat}_imputed_domain'
    })

imputation_metadata_df = pd.DataFrame(imputation_metadata)

print('=== IMPUTATION METADATA REPORT ===\n')
print(imputation_metadata_df.to_string(index=False))
print(f'\nTotal features imputed: {len(imputation_metadata_df)}')
print(f'Total imputation flag columns created: {len(imputation_metadata_df)}')
print(f'\nImputation strategies used:')
print(f'  - Forward-Fill: {len(ffill_features)} features')
print(f'  - Median: {len(median_features)} features')
print(f'  - KNN: {len(knn_features_list)} features')
print(f'  - Domain-Specific: {len(business_features_list)} features')