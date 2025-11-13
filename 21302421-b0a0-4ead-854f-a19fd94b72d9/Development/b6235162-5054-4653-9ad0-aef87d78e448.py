import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Calculate leverage ratio (liabilities/assets) and profitability (net profit/revenue)
loan_df_calc = loan_df.copy()
loan_df_calc['leverage_ratio'] = loan_df_calc['TOTAL_LIABILITIES'] / (loan_df_calc['TOTAL_ASSETS'] + 1)
loan_df_calc['profit_margin'] = loan_df_calc['NET_PROFIT'] / (loan_df_calc['BUSINESS_REVENUE'] + 1)

# Filter out extreme outliers for visualization clarity
leverage_filtered = loan_df_calc[(loan_df_calc['leverage_ratio'] < 2) & (loan_df_calc['profit_margin'] < 2) & (loan_df_calc['profit_margin'] > -2)]

# Scatter plot: Leverage vs Profitability
plt.figure(figsize=(10, 7))
plt.scatter(leverage_filtered['leverage_ratio'], leverage_filtered['profit_margin'], 
            alpha=0.5, s=30, c='darkgreen')
plt.xlabel('Leverage Ratio (Liabilities/Assets)', fontsize=12)
plt.ylabel('Profit Margin (Net Profit/Revenue)', fontsize=12)
plt.title('Bivariate: Leverage vs Profitability', fontsize=14, fontweight='bold')
plt.axhline(y=0, color='red', linestyle='--', alpha=0.5)
plt.axvline(x=1, color='red', linestyle='--', alpha=0.5)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

leverage_profit_corr = leverage_filtered[['leverage_ratio', 'profit_margin']].corr().iloc[0, 1]
print(f'Correlation: {leverage_profit_corr:.4f}')
print(f'Filtered to {len(leverage_filtered)} records (removed extreme outliers)')