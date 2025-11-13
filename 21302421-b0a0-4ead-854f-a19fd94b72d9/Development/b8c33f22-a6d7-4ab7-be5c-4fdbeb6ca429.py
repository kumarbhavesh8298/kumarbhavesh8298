import pandas as pd

# Find numeric columns
candidate_scaling_cols = []
for xyz in imputed_df.columns:
    if xyz == 'CUST_ID' or '_imputed_' in xyz:
        continue
    if imputed_df[xyz].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[xyz]):
        candidate_scaling_cols.append(xyz)

print(f'Numeric: {len(candidate_scaling_cols)}')