import pandas as pd

# Identify numeric columns
numeric_scale_list = []
for colname_iter in imputed_df.columns:
    if colname_iter == 'CUST_ID' or '_imputed_' in colname_iter:
        continue
    if imputed_df[colname_iter].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[colname_iter]):
        numeric_scale_list.append(colname_iter)

print(f'Numeric columns: {len(numeric_scale_list)}')