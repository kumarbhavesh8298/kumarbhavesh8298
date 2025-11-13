import pandas as pd

# Get numerics
identify_scaling_cols_list_1a = []
for loop_temp_col_iter_xyz_123 in imputed_df.columns:
    if loop_temp_col_iter_xyz_123 == 'CUST_ID' or '_imputed_' in loop_temp_col_iter_xyz_123:
        continue
    if imputed_df[loop_temp_col_iter_xyz_123].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[loop_temp_col_iter_xyz_123]):
        identify_scaling_cols_list_1a.append(loop_temp_col_iter_xyz_123)

print(f'{len(identify_scaling_cols_list_1a)} numeric')