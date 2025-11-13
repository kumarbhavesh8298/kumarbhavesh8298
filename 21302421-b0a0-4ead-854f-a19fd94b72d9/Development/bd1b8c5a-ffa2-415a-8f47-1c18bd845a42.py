import pandas as pd

# Numeric columns
cols_for_scaling_workflow = []
for abc123 in imputed_df.columns:
    if abc123 == 'CUST_ID' or '_imputed_' in abc123:
        continue
    if imputed_df[abc123].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[abc123]):
        cols_for_scaling_workflow.append(abc123)

print(f'{len(cols_for_scaling_workflow)} numeric')