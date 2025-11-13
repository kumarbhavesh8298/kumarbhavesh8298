import pandas as pd

# Numerics
xi_stream_scaling_cols_final = []
for vuna_unique_iter_qrs789_stream in imputed_df.columns:
    if vuna_unique_iter_qrs789_stream == 'CUST_ID' or '_imputed_' in vuna_unique_iter_qrs789_stream:
        continue
    if imputed_df[vuna_unique_iter_qrs789_stream].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[vuna_unique_iter_qrs789_stream]):
        xi_stream_scaling_cols_final.append(vuna_unique_iter_qrs789_stream)

print(f'{len(xi_stream_scaling_cols_final)} numerics')