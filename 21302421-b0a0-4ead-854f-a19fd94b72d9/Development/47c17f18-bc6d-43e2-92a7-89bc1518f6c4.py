import pandas as pd

# Numeric columns
task_alpha_scaling_numcols_list = []
for super_unique_iter_var_pqr in imputed_df.columns:
    if super_unique_iter_var_pqr == 'CUST_ID' or '_imputed_' in super_unique_iter_var_pqr:
        continue
    if imputed_df[super_unique_iter_var_pqr].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[super_unique_iter_var_pqr]):
        task_alpha_scaling_numcols_list.append(super_unique_iter_var_pqr)

print(f'{len(task_alpha_scaling_numcols_list)} numerics')