import pandas as pd

# Find numerics
kappa_run_find_scaling_numerics = []
for zetta_unique_var_efg567 in imputed_df.columns:
    if zetta_unique_var_efg567 == 'CUST_ID' or '_imputed_' in zetta_unique_var_efg567:
        continue
    if imputed_df[zetta_unique_var_efg567].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[zetta_unique_var_efg567]):
        kappa_run_find_scaling_numerics.append(zetta_unique_var_efg567)

print(f'{len(kappa_run_find_scaling_numerics)} numerics')