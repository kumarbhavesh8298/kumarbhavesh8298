import pandas as pd

# Select numerics
delta_select_numerics_for_scale = []
for ultra_unique_iteration_jkl in imputed_df.columns:
    if ultra_unique_iteration_jkl == 'CUST_ID' or '_imputed_' in ultra_unique_iteration_jkl:
        continue
    if imputed_df[ultra_unique_iteration_jkl].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[ultra_unique_iteration_jkl]):
        delta_select_numerics_for_scale.append(ultra_unique_iteration_jkl)

print(f'{len(delta_select_numerics_for_scale)} numerics')