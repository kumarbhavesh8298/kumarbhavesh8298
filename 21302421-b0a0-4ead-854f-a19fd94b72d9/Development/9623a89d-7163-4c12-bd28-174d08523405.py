import pandas as pd

# Numerics
iota_task_scaling_numeric_columns = []
for exa_unique_loop_bcd234 in imputed_df.columns:
    if exa_unique_loop_bcd234 == 'CUST_ID' or '_imputed_' in exa_unique_loop_bcd234:
        continue
    if imputed_df[exa_unique_loop_bcd234].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[exa_unique_loop_bcd234]):
        iota_task_scaling_numeric_columns.append(exa_unique_loop_bcd234)

print(f'{len(iota_task_scaling_numeric_columns)} numerics')