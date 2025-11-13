import pandas as pd
import numpy as np

# Binary flags for outlier conditions

outlier_bin_df = imputed_df.copy()

# 1. High leverage: TOTAL_LIABILITIES / TOTAL_ASSETS > 0.75
outlier_bin_df['is_high_leverage'] = (
    (outlier_bin_df['TOTAL_LIABILITIES'] / outlier_bin_df['TOTAL_ASSETS']) > 0.75
).astype(int)

# 2. Negative profit: NET_PROFIT < 0
outlier_bin_df['is_negative_profit'] = (outlier_bin_df['NET_PROFIT'] < 0).astype(int)

# 3. Over limit: BALANCE > FUND_AMT
outlier_bin_df['is_overlimit'] = (outlier_bin_df['BALANCE'] > outlier_bin_df['FUND_AMT']).astype(int)

print(f'is_high_leverage: {outlier_bin_df["is_high_leverage"].sum()}')
print(f'is_negative_profit: {outlier_bin_df["is_negative_profit"].sum()}')
print(f'is_overlimit: {outlier_bin_df["is_overlimit"].sum()}')