import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Box plot: LOAN_STATUS vs BALANCE
plt.figure(figsize=(12, 7))
sns.boxplot(data=loan_df, x='LOAN_STATUS', y='BALANCE', palette='coolwarm')
plt.xlabel('Loan Status', fontsize=12)
plt.ylabel('Current Balance', fontsize=12)
plt.title('Bivariate: Loan Status vs Balance', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.ticklabel_format(style='plain', axis='y')
plt.tight_layout()
plt.show()

# Calculate statistics by loan status
status_stats = loan_df.groupby('LOAN_STATUS')['BALANCE'].agg(['mean', 'median', 'count']).round(2)
print(f'Balance by Loan Status:\n{status_stats}')