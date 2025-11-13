import pandas as pd

# Numerics
nu_batch_identify_scaling_cols = []
for weka_unique_loop_nop456_batch in imputed_df.columns:
    if weka_unique_loop_nop456_batch == 'CUST_ID' or '_imputed_' in weka_unique_loop_nop456_batch:
        continue
    if imputed_df[weka_unique_loop_nop456_batch].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[weka_unique_loop_nop456_batch]):
        nu_batch_identify_scaling_cols.append(weka_unique_loop_nop456_batch)

print(f'{len(nu_batch_identify_scaling_cols)} numerics')