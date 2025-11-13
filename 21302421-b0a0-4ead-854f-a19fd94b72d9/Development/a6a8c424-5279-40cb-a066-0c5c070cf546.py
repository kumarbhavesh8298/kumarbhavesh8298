import pandas as pd
import numpy as np

# No financial ratio features exist in the dataset based on our analysis
# The task mentions ROI and DRAWING_POWER, but these don't exist
# Let's focus on COLLATERAL_VALUE which is a financial feature

# Apply median imputation for COLLATERAL_VALUE (financial feature)
financial_features = ['COLLATERAL_VALUE']

median_imputed_count = {}
for feature in financial_features:
    if feature in imputed_df.columns:
        before_null = imputed_df[feature].isnull().sum()
        median_value = imputed_df[feature].median()
        imputed_df[feature] = imputed_df[feature].fillna(median_value)
        after_null = imputed_df[feature].isnull().sum()
        median_imputed_count[feature] = before_null - after_null
        
        # Create imputation flag
        imputed_df[f'{feature}_imputed_median'] = loan_df_with_missing[feature].isnull().astype(int)
        print(f'{feature}: imputed {before_null} values with median {median_value:.2f}')

print(f'\nMedian imputation completed for {len(financial_features)} financial features')
print(f'Total values imputed: {sum(median_imputed_count.values())}')