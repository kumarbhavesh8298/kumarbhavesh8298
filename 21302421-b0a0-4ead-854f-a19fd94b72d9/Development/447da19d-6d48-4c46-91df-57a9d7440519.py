import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Scatter plot: COLLATERAL_VALUE vs FUND_AMT
plt.figure(figsize=(10, 7))
plt.scatter(loan_df['COLLATERAL_VALUE'], loan_df['FUND_AMT'], alpha=0.5, s=30, c='orange')
plt.xlabel('Collateral Value', fontsize=12)
plt.ylabel('Fund Amount', fontsize=12)
plt.title('Bivariate: Collateral Value vs Fund Amount', fontsize=14, fontweight='bold')
plt.ticklabel_format(style='plain', axis='both')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Calculate correlation
collateral_fund_corr = loan_df[['COLLATERAL_VALUE', 'FUND_AMT']].corr().iloc[0, 1]
print(f'Correlation: {collateral_fund_corr:.4f}')