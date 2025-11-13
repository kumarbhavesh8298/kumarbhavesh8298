import pandas as pd

# Find numeric columns
scaling_numeric_list_v1 = []
for qwerty123_abc in imputed_df.columns:
    if qwerty123_abc == 'CUST_ID' or '_imputed_' in qwerty123_abc:
        continue
    if imputed_df[qwerty123_abc].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[qwerty123_abc]):
        scaling_numeric_list_v1.append(qwerty123_abc)

print(f'{len(scaling_numeric_list_v1)} numeric cols')