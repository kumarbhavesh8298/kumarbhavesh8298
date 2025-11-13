import pandas as pd

# Numeric columns
nums_scale_2024_v1_final = []
for temp_iter_col_name_unique in imputed_df.columns:
    if temp_iter_col_name_unique == 'CUST_ID' or '_imputed_' in temp_iter_col_name_unique:
        continue
    if imputed_df[temp_iter_col_name_unique].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[temp_iter_col_name_unique]):
        nums_scale_2024_v1_final.append(temp_iter_col_name_unique)

print(f'{len(nums_scale_2024_v1_final)} numeric')