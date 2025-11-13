import pandas as pd

# Get numeric columns
workflow_numerics_v2_scaling_list = []
for very_unique_loop_var_789 in imputed_df.columns:
    if very_unique_loop_var_789 == 'CUST_ID' or '_imputed_' in very_unique_loop_var_789:
        continue
    if imputed_df[very_unique_loop_var_789].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[very_unique_loop_var_789]):
        workflow_numerics_v2_scaling_list.append(very_unique_loop_var_789)

print(f'{len(workflow_numerics_v2_scaling_list)} numerics')