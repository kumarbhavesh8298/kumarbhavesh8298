import pandas as pd
import numpy as np

# Create a copy for imputation
imputed_df = loan_df_with_missing.copy()

# Identify time-series ordered features (those with dates)
# For this dataset, we'll sort by CUST_OPN_DT to maintain time order
imputed_df = imputed_df.sort_values('CUST_OPN_DT')

# Features that benefit from forward-fill (temporal continuity)
# These are features that may have temporal patterns
time_sensitive_features = ['DEBT_TO_INCOME', 'YEARS_EMPLOYED']

# Apply forward fill for time-series features
forward_filled_count = {}
for feature in time_sensitive_features:
    if feature in imputed_df.columns:
        before_null = imputed_df[feature].isnull().sum()
        imputed_df[feature] = imputed_df[feature].fillna(method='ffill')
        after_null = imputed_df[feature].isnull().sum()
        forward_filled_count[feature] = before_null - after_null

# Create imputation flags for forward-filled features
for feature in time_sensitive_features:
    if feature in loan_df_with_missing.columns:
        imputed_df[f'{feature}_imputed_ffill'] = loan_df_with_missing[feature].isnull().astype(int)

print(f'Forward-fill imputation completed for {len(time_sensitive_features)} features')
print(f'Values imputed: {sum(forward_filled_count.values())}')
for feature, count in forward_filled_count.items():
    print(f'  {feature}: {count} values')