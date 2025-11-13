import pandas as pd

# Identify numeric features for scaling
scols = [x for x in imputed_df.columns 
         if x != 'CUST_ID'
         and '_imputed_' not in x
         and imputed_df[x].dtype != 'datetime64[ns]'
         and pd.api.types.is_numeric_dtype(imputed_df[x])]

print(f'Numeric columns identified: {len(scols)}')