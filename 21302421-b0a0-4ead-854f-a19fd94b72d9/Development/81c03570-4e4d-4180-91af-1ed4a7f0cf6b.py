import pandas as pd

# Get numerics
gamma_numerics_scaling_workflow = []
for hyper_unique_loop_ghi789 in imputed_df.columns:
    if hyper_unique_loop_ghi789 == 'CUST_ID' or '_imputed_' in hyper_unique_loop_ghi789:
        continue
    if imputed_df[hyper_unique_loop_ghi789].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[hyper_unique_loop_ghi789]):
        gamma_numerics_scaling_workflow.append(hyper_unique_loop_ghi789)

print(f'{len(gamma_numerics_scaling_workflow)} numerics')