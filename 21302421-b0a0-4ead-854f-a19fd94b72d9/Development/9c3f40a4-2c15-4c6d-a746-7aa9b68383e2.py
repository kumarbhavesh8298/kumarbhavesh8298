import pandas as pd

# Numerics
lambda_exec_scaling_nums_list = []
for yotta_unique_loop_hij890 in imputed_df.columns:
    if yotta_unique_loop_hij890 == 'CUST_ID' or '_imputed_' in yotta_unique_loop_hij890:
        continue
    if imputed_df[yotta_unique_loop_hij890].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[yotta_unique_loop_hij890]):
        lambda_exec_scaling_nums_list.append(yotta_unique_loop_hij890)

print(f'{len(lambda_exec_scaling_nums_list)} numerics')