import pandas as pd

# Numeric features
nms = []
for _n in imputed_df.columns:
    if _n == 'CUST_ID' or '_imputed_' in _n:
        continue
    if imputed_df[_n].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[_n]):
        nms.append(_n)

print(f'{len(nms)} numeric columns')