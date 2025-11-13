import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Scatter plot: TOTAL_ASSETS vs ANNUAL_REVENUE (using ANNUAL_INCOME as proxy for business revenue)
plt.figure(figsize=(10, 7))
plt.scatter(loan_df['TOTAL_ASSETS'], loan_df['BUSINESS_REVENUE'], alpha=0.5, s=30, c='steelblue')
plt.xlabel('Total Assets', fontsize=12)
plt.ylabel('Business Revenue', fontsize=12)
plt.title('Bivariate: Total Assets vs Business Revenue', fontsize=14, fontweight='bold')
plt.ticklabel_format(style='plain', axis='both')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Calculate correlation
assets_revenue_corr = loan_df[['TOTAL_ASSETS', 'BUSINESS_REVENUE']].corr().iloc[0, 1]
print(f'Correlation: {assets_revenue_corr:.4f}')