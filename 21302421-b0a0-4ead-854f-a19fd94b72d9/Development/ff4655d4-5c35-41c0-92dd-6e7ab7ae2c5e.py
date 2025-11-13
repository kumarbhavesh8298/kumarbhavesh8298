import pandas as pd
import numpy as np

# IQR method for financial features: FUND_AMT, BALANCE, BUSINESS_REVENUE (not ANNUAL_REVENUE), OPERATING_PROFIT
financial_cols_iqr = ['FUND_AMT', 'BALANCE', 'BUSINESS_REVENUE', 'OPERATING_PROFIT']

# Create IQR outlier flags
iqr_outlier_flags = pd.DataFrame(index=imputed_df.index)

for _col in financial_cols_iqr:
    Q1 = imputed_df[_col].quantile(0.25)
    Q3 = imputed_df[_col].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Flag outliers (1 = outlier, 0 = normal)
    iqr_outlier_flags[f'{_col}_iqr_outlier'] = (
        (imputed_df[_col] < lower_bound) | (imputed_df[_col] > upper_bound)
    ).astype(int)
    
    outlier_count = iqr_outlier_flags[f'{_col}_iqr_outlier'].sum()
    print(f'{_col}: {outlier_count} outliers detected (Q1={Q1:.2f}, Q3={Q3:.2f}, IQR={IQR:.2f})')

# Count total IQR outliers per row
iqr_outlier_flags['iqr_outlier_count'] = iqr_outlier_flags.filter(like='_iqr_outlier').sum(axis=1)

print(f'\nIQR outlier detection completed for {len(financial_cols_iqr)} financial features')
print(f'Rows with at least 1 IQR outlier: {(iqr_outlier_flags["iqr_outlier_count"] > 0).sum()}')