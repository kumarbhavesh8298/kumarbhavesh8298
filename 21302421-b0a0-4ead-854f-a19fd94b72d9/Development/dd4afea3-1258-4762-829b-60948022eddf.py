import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Violin plot: DEBT_TO_INCOME by LOAN_STATUS (focus on default indicator)
plt.figure(figsize=(12, 7))
sns.violinplot(data=loan_df, x='LOAN_STATUS', y='DEBT_TO_INCOME', palette='muted')
plt.xlabel('Loan Status', fontsize=12)
plt.ylabel('Debt-to-Income Ratio', fontsize=12)
plt.title('Bivariate: Debt-to-Income Ratio by Loan Status', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Statistics
dti_stats = loan_df.groupby('LOAN_STATUS')['DEBT_TO_INCOME'].agg(['mean', 'median']).round(4)
print(f'DTI by Loan Status:\n{dti_stats}')