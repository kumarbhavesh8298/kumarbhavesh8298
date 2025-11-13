import pandas as pd

# Numeric columns
get_numerics_for_scaling_abc_xyz = []
for unique_loop_variable_12345 in imputed_df.columns:
    if unique_loop_variable_12345 == 'CUST_ID' or '_imputed_' in unique_loop_variable_12345:
        continue
    if imputed_df[unique_loop_variable_12345].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[unique_loop_variable_12345]):
        get_numerics_for_scaling_abc_xyz.append(unique_loop_variable_12345)

print(f'{len(get_numerics_for_scaling_abc_xyz)} numerics')