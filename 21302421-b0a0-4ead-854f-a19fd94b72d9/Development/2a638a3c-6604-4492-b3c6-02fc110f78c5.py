import pandas as pd

# Identify numeric columns
numeric_columns_task_scaling = []
for asdfgh_xyz_abc123 in imputed_df.columns:
    if asdfgh_xyz_abc123 == 'CUST_ID' or '_imputed_' in asdfgh_xyz_abc123:
        continue
    if imputed_df[asdfgh_xyz_abc123].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[asdfgh_xyz_abc123]):
        numeric_columns_task_scaling.append(asdfgh_xyz_abc123)

print(f'{len(numeric_columns_task_scaling)} numerics')