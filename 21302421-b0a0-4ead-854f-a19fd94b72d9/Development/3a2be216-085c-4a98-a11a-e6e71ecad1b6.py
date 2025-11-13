import pandas as pd

# Numeric columns
num_features_for_scaling_nov2024 = []
for lmnop_qrs_tuv_wx_yz in imputed_df.columns:
    if lmnop_qrs_tuv_wx_yz == 'CUST_ID' or '_imputed_' in lmnop_qrs_tuv_wx_yz:
        continue
    if imputed_df[lmnop_qrs_tuv_wx_yz].dtype == 'datetime64[ns]':
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[lmnop_qrs_tuv_wx_yz]):
        num_features_for_scaling_nov2024.append(lmnop_qrs_tuv_wx_yz)

print(f'{len(num_features_for_scaling_nov2024)} numerics')