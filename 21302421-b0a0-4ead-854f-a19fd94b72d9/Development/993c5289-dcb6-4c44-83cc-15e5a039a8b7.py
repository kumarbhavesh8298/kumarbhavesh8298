import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Scatter plot: CREDIT_SCORE vs INTEREST_RATE
plt.figure(figsize=(10, 7))
plt.scatter(loan_df['CREDIT_SCORE'], loan_df['INTEREST_RATE'], alpha=0.5, s=30, c='purple')
plt.xlabel('Credit Score', fontsize=12)
plt.ylabel('Interest Rate (%)', fontsize=12)
plt.title('Bivariate: Credit Score vs Interest Rate', fontsize=14, fontweight='bold')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Calculate correlation
credit_rate_corr = loan_df[['CREDIT_SCORE', 'INTEREST_RATE']].corr().iloc[0, 1]
print(f'Correlation: {credit_rate_corr:.4f}')