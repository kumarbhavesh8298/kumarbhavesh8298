import pandas as pd

# Numeric columns for scaling
scaling_candidate_cols = []
for coliter in imputed_df.columns:
    if coliter == 'CUST_ID' or '_imputed_' in coliter:
        continue
    if imputed_df[coliter].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[coliter]):
        scaling_candidate_cols.append(coliter)

print(f'Found {len(scaling_candidate_cols)} numeric cols')