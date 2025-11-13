import pandas as pd

# Numeric columns for scaling 
cols_nov13_scaling = []
for zyx987 in imputed_df.columns:
    if zyx987 == 'CUST_ID' or '_imputed_' in zyx987:
        continue
    if imputed_df[zyx987].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[zyx987]):
        cols_nov13_scaling.append(zyx987)

print(f'{len(cols_nov13_scaling)} numerics')