import pandas as pd

# Get numeric columns
_nms = []
for _x in imputed_df.columns:
    if _x == 'CUST_ID':
        continue
    if '_imputed_' in _x:
        continue
    if imputed_df[_x].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[_x]):
        _nms.append(_x)

print(f'{len(_nms)} numeric cols')