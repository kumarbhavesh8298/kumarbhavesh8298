import pandas as pd
import numpy as np

# Note: The task mentions MARITAL_STATUS, INDUSTRY_SECTOR, and AREACATEGORY
# However, based on our missing data analysis, only categorical features 
# that exist and have missing data should be imputed
# From our data, we found no missing categorical features, but let's handle them if they exist

# Check for categorical columns with missing values
categorical_cols = ['MARITAL_STATUS', 'INDUSTRY_SECTOR', 'OCCP_CODE', 'EMPLOYMENT_STATUS']
mode_imputed_count = {}

for feature in categorical_cols:
    if feature in imputed_df.columns and imputed_df[feature].isnull().sum() > 0:
        before_null = imputed_df[feature].isnull().sum()
        mode_value = imputed_df[feature].mode()[0]
        imputed_df[feature] = imputed_df[feature].fillna(mode_value)
        after_null = imputed_df[feature].isnull().sum()
        mode_imputed_count[feature] = before_null - after_null
        
        # Create imputation flag
        imputed_df[f'{feature}_imputed_mode'] = loan_df_with_missing[feature].isnull().astype(int)
        print(f'{feature}: imputed {before_null} values with mode "{mode_value}"')

if len(mode_imputed_count) == 0:
    print('No categorical features with missing values found')
else:
    print(f'\nMode imputation completed for {len(mode_imputed_count)} categorical features')
    print(f'Total values imputed: {sum(mode_imputed_count.values())}')