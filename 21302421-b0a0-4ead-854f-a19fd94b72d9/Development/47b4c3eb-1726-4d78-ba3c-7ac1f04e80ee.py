import pandas as pd

# Find numerics
zeta_phase_scaling_numeric_list = []
for giga_unique_loop_stu345 in imputed_df.columns:
    if giga_unique_loop_stu345 == 'CUST_ID' or '_imputed_' in giga_unique_loop_stu345:
        continue
    if imputed_df[giga_unique_loop_stu345].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[giga_unique_loop_stu345]):
        zeta_phase_scaling_numeric_list.append(giga_unique_loop_stu345)

print(f'{len(zeta_phase_scaling_numeric_list)} numerics')