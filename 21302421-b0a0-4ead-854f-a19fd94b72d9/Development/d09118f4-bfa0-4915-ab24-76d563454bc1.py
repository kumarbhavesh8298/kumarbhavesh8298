import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Box plot: LOAN_PURPOSE vs BALANCE
plt.figure(figsize=(12, 7))
sns.boxplot(data=loan_df, x='LOAN_PURPOSE', y='BALANCE', palette='viridis')
plt.xlabel('Loan Purpose', fontsize=12)
plt.ylabel('Current Balance', fontsize=12)
plt.title('Bivariate: Loan Purpose vs Balance', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.ticklabel_format(style='plain', axis='y')
plt.tight_layout()
plt.show()

# Calculate median by purpose
purpose_median = loan_df.groupby('LOAN_PURPOSE')['BALANCE'].median().sort_values(ascending=False)
print(f'Median Balance by Loan Purpose:\n{purpose_median}')