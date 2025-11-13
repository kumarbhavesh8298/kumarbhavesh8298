import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Select top 10 most important features based on business relevance
top_features = [
    'FUND_AMT', 'BALANCE', 'TOTAL_ASSETS', 'ANNUAL_INCOME',
    'CREDIT_SCORE', 'INTEREST_RATE', 'DEBT_TO_INCOME',
    'COLLATERAL_VALUE', 'NET_PROFIT', 'CREDIT_UTILIZATION'
]

# Create pairplot with subset of data for clarity
pairplot_data = loan_df[top_features].sample(n=min(500, len(loan_df)), random_state=42)

# Create pairplot
sns.pairplot(pairplot_data, diag_kind='kde', plot_kws={'alpha': 0.4, 's': 20}, corner=True)
plt.suptitle('Pairplot: Top 10 Important Features', y=1.001, fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

print(f'Pairplot created for {len(top_features)} features using {len(pairplot_data)} samples')