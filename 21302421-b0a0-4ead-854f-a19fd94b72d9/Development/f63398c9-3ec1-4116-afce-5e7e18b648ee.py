import pandas as pd

# Identify numeric features (excluding IDs dates, imputation flags)
scale_cols = [c for c in imputed_df.columns 
              if c != 'CUST_ID'
              and '_imputed_' not in c
              and imputed_df[c].dtype != 'datetime64[ns]'
              and pd.api.types.is_numeric_dtype(imputed_df[c])]

print(f'Found {len(scale_cols)} numeric columns for scaling')