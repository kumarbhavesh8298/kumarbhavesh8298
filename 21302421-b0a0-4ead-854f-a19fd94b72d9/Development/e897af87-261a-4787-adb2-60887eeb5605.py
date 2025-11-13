import pandas as pd

# Identify numerics
epsilon_identify_scaling_numerics = []
for mega_unique_var_mno012 in imputed_df.columns:
    if mega_unique_var_mno012 == 'CUST_ID' or '_imputed_' in mega_unique_var_mno012:
        continue
    if imputed_df[mega_unique_var_mno012].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[mega_unique_var_mno012]):
        epsilon_identify_scaling_numerics.append(mega_unique_var_mno012)

print(f'{len(epsilon_identify_scaling_numerics)} numerics')