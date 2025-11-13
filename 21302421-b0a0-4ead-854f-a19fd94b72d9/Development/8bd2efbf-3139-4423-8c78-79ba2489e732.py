import pandas as pd

# Find numeric columns
beta_task_numerics_scaling_cols = []
for extremely_unique_var_def456 in imputed_df.columns:
    if extremely_unique_var_def456 == 'CUST_ID' or '_imputed_' in extremely_unique_var_def456:
        continue
    if imputed_df[extremely_unique_var_def456].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[extremely_unique_var_def456]):
        beta_task_numerics_scaling_cols.append(extremely_unique_var_def456)

print(f'{len(beta_task_numerics_scaling_cols)} numerics')