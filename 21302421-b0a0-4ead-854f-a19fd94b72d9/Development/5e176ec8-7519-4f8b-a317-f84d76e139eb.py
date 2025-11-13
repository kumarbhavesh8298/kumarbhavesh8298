import pandas as pd

# Numerics
mu_proc_scaling_numeric_features = []
for xona_unique_var_klm123_iter in imputed_df.columns:
    if xona_unique_var_klm123_iter == 'CUST_ID' or '_imputed_' in xona_unique_var_klm123_iter:
        continue
    if imputed_df[xona_unique_var_klm123_iter].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[xona_unique_var_klm123_iter]):
        mu_proc_scaling_numeric_features.append(xona_unique_var_klm123_iter)

print(f'{len(mu_proc_scaling_numeric_features)} numerics')