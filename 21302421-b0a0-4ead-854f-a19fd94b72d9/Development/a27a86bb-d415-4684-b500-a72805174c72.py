import pandas as pd

# Get numerics
eta_v3_get_scaling_numerics_final = []
for tera_unique_var_vwx678 in imputed_df.columns:
    if tera_unique_var_vwx678 == 'CUST_ID' or '_imputed_' in tera_unique_var_vwx678:
        continue
    if imputed_df[tera_unique_var_vwx678].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[tera_unique_var_vwx678]):
        eta_v3_get_scaling_numerics_final.append(tera_unique_var_vwx678)

print(f'{len(eta_v3_get_scaling_numerics_final)} numerics')