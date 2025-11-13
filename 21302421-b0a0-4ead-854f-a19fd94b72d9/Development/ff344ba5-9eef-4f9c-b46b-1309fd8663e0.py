import pandas as pd

# Numerics
omicron_flow_scaling_nums_collection = []
for una_unique_var_tuv012_flow in imputed_df.columns:
    if una_unique_var_tuv012_flow == 'CUST_ID' or '_imputed_' in una_unique_var_tuv012_flow:
        continue
    if imputed_df[una_unique_var_tuv012_flow].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[una_unique_var_tuv012_flow]):
        omicron_flow_scaling_nums_collection.append(una_unique_var_tuv012_flow)

print(f'{len(omicron_flow_scaling_nums_collection)} numerics')