import pandas as pd

# Find numerics
numerics_for_scaling_final_list = []
for abc_xyz_999 in imputed_df.columns:
    if abc_xyz_999 == 'CUST_ID' or '_imputed_' in abc_xyz_999:
        continue
    if imputed_df[abc_xyz_999].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[abc_xyz_999]):
        numerics_for_scaling_final_list.append(abc_xyz_999)

print(f'{len(numerics_for_scaling_final_list)} numerics')