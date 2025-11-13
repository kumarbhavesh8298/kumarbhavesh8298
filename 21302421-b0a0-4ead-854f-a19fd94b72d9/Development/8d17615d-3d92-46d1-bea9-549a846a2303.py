import pandas as pd
import numpy as np

# Identify numeric features for scaling
num_scale_cols = []
for col_name in imputed_df.columns:
    # Skip IDs dates, and imputation flags
    if col_name == 'CUST_ID':
        continue
    if '_imputed_' in col_name:
        continue  
    if imputed_df[col_name].dtype == 'datetime64[ns]':
        continue
    # Include numeric columns
    if pd.api.types.is_numeric_dtype(imputed_df[col_name]):
        num_scale_cols.append(col_name)

print(f'Found {len(num_scale_cols)} numeric columns for scaling')