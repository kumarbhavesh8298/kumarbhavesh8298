import pandas as pd

# Get numeric columns for scaling
scaling_workflow_2024_cols = []
for q1q2q3 in imputed_df.columns:
    if q1q2q3 == 'CUST_ID' or '_imputed_' in q1q2q3:
        continue
    if imputed_df[q1q2q3].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[q1q2q3]):
        scaling_workflow_2024_cols.append(q1q2q3)

print(f'{len(scaling_workflow_2024_cols)} numeric cols')