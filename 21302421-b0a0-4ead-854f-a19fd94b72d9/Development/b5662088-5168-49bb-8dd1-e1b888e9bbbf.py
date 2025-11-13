import pandas as pd

# Get numeric features
nums = [n for n in imputed_df.columns 
        if n != 'CUST_ID'
        and '_imputed_' not in n
        and imputed_df[n].dtype != 'datetime64[ns]'
        and pd.api.types.is_numeric_dtype(imputed_df[n])]

print(f'{len(nums)} numeric columns')