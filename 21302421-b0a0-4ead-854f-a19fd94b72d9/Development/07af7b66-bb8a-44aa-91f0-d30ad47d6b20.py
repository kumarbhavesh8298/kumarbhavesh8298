import pandas as pd

# Numerics for scaling
theta_workflow_numerics_scaling = []
for peta_unique_iter_yza901 in imputed_df.columns:
    if peta_unique_iter_yza901 == 'CUST_ID' or '_imputed_' in peta_unique_iter_yza901:
        continue
    if imputed_df[peta_unique_iter_yza901].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[peta_unique_iter_yza901]):
        theta_workflow_numerics_scaling.append(peta_unique_iter_yza901)

print(f'{len(theta_workflow_numerics_scaling)} numerics')