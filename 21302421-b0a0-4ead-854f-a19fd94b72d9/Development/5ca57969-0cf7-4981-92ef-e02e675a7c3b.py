import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Scatter plot: BALANCE vs COLLATERAL_VALUE (proxy for sanction limit)
plt.figure(figsize=(10, 7))
plt.scatter(loan_df['BALANCE'], loan_df['COLLATERAL_VALUE'], alpha=0.5, s=30, c='coral')
plt.xlabel('Current Balance', fontsize=12)
plt.ylabel('Collateral Value (Sanction Limit Proxy)', fontsize=12)
plt.title('Bivariate: Balance vs Collateral Value', fontsize=14, fontweight='bold')
plt.ticklabel_format(style='plain', axis='both')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Calculate correlation
balance_collateral_corr = loan_df[['BALANCE', 'COLLATERAL_VALUE']].corr().iloc[0, 1]
print(f'Correlation: {balance_collateral_corr:.4f}')