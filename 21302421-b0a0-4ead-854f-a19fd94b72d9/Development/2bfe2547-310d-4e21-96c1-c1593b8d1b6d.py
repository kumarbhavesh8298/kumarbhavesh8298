import pandas as pd
import numpy as np

# Identify all numeric features from imputed_df (excluding IDs, dates, flags)
numeric_scale_features = []
for c in imputed_df.columns:
    if c == 'CUST_ID' or '_imputed_' in c:
        continue
    if imputed_df[c].dtype in ['datetime64[ns]']:
        continue
    if pd.api.types.is_numeric_dtype(imputed_df[c]):
        numeric_scale_features.append(c)

print(f'Identified {len(numeric_scale_features)} numeric features for scaling')
print(f'First 10: {numeric_scale_features[:10]}')