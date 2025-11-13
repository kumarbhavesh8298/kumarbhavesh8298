import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Box plot: EMPLOYMENT_STATUS vs ANNUAL_INCOME
plt.figure(figsize=(12, 7))
sns.boxplot(data=loan_df, x='EMPLOYMENT_STATUS', y='ANNUAL_INCOME', palette='Pastel1')
plt.xlabel('Employment Status', fontsize=12)
plt.ylabel('Annual Income', fontsize=12)
plt.title('Bivariate: Employment Status vs Annual Income', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.ticklabel_format(style='plain', axis='y')
plt.tight_layout()
plt.show()

# Calculate statistics
employment_income_stats = loan_df.groupby('EMPLOYMENT_STATUS')['ANNUAL_INCOME'].agg(['mean', 'median']).round(2)
print(f'Income by Employment Status:\n{employment_income_stats}')