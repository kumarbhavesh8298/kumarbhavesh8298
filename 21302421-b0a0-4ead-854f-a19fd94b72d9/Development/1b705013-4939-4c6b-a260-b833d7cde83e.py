import pandas as pd

# Create list of numeric columns to scale
numeric_cols_to_scale = []
for iter_col_name in imputed_df.columns:
    if iter_col_name == 'CUST_ID' or '_imputed_' in iter_col_name:
        continue
    if imputed_df[iter_col_name].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[iter_col_name]):
        numeric_cols_to_scale.append(iter_col_name)

print(f'Numeric columns identified: {len(numeric_cols_to_scale)}')