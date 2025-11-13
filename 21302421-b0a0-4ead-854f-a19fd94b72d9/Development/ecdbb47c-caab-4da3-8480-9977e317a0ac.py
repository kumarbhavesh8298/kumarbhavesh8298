import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Scatter plot: ANNUAL_INCOME vs FUND_AMT
plt.figure(figsize=(10, 7))
plt.scatter(loan_df['ANNUAL_INCOME'], loan_df['FUND_AMT'], alpha=0.5, s=30, c='teal')
plt.xlabel('Annual Income', fontsize=12)
plt.ylabel('Fund Amount', fontsize=12)
plt.title('Bivariate: Annual Income vs Fund Amount', fontsize=14, fontweight='bold')
plt.ticklabel_format(style='plain', axis='both')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Calculate correlation
income_fund_corr = loan_df[['ANNUAL_INCOME', 'FUND_AMT']].corr().iloc[0, 1]
print(f'Correlation: {income_fund_corr:.4f}')