import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Scatter plot: BUSINESS_REVENUE vs BUSINESS_EXPENSES
plt.figure(figsize=(10, 7))
plt.scatter(loan_df['BUSINESS_REVENUE'], loan_df['BUSINESS_EXPENSES'], 
            alpha=0.5, s=30, c='brown')
plt.xlabel('Business Revenue', fontsize=12)
plt.ylabel('Business Expenses', fontsize=12)
plt.title('Bivariate: Business Revenue vs Expenses', fontsize=14, fontweight='bold')
plt.ticklabel_format(style='plain', axis='both')

# Add diagonal line for reference (break-even point)
_max_val = max(loan_df['BUSINESS_REVENUE'].max(), loan_df['BUSINESS_EXPENSES'].max())
plt.plot([0, _max_val], [0, _max_val], 'r--', alpha=0.5, label='Break-even')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Calculate correlation
revenue_expense_corr = loan_df[['BUSINESS_REVENUE', 'BUSINESS_EXPENSES']].corr().iloc[0, 1]
print(f'Correlation: {revenue_expense_corr:.4f}')