import pandas as pd

# Identify numeric columns
numerical_features_scaling = []
for col_xyz123 in imputed_df.columns:
    if col_xyz123 == 'CUST_ID' or '_imputed_' in col_xyz123:
        continue
    if imputed_df[col_xyz123].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[col_xyz123]):
        numerical_features_scaling.append(col_xyz123)

print(f'{len(numerical_features_scaling)} numeric features')