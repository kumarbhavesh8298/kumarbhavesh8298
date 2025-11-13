import pandas as pd

# Identify numeric columns for scaling
_numeric_cols_list = []
for _col_iter in imputed_df.columns:
    if _col_iter == 'CUST_ID':
        continue
    if '_imputed_' in _col_iter:
        continue
    if imputed_df[_col_iter].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[_col_iter]):
        _numeric_cols_list.append(_col_iter)

print(f'Numeric columns: {len(_numeric_cols_list)}')