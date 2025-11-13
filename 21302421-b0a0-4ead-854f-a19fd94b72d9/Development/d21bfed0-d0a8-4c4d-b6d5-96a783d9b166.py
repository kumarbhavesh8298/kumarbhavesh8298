import pandas as pd

# Identify numeric features for scaling
to_scale = [nm for nm in imputed_df.columns 
            if nm != 'CUST_ID'
            and '_imputed_' not in nm
            and imputed_df[nm].dtype != 'datetime64[ns]'
            and pd.api.types.is_numeric_dtype(imputed_df[nm])]

print(f'Identified {len(to_scale)} numeric columns')