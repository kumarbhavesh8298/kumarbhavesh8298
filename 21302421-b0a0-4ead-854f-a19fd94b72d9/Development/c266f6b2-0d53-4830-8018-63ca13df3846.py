import pandas as pd
import numpy as np

# Identify all numeric features from imputed_df
# Exclude ID fields, date fields, and imputation flag columns

numeric_feats = []
for col in imputed_df.columns:
    # Skip ID, date fields, and imputation flags
    if col in ['CUST_ID'] or '_imputed_' in col or imputed_df[col].dtype in ['datetime64[ns]']:
        continue
    # Include numeric types
    if pd.api.types.is_numeric_dtype(imputed_df[col]):
        numeric_feats.append(col)

print(f'Identified {len(numeric_feats)} numeric features for scaling:')
for _f in numeric_feats[:10]:
    print(f'  - {_f}')
if len(numeric_feats) > 10:
    print(f'  ... and {len(numeric_feats) - 10} more')

# Store numeric feature list for downstream use
scaling_numeric_cols = numeric_feats