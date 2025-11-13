import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Box plot: INDUSTRY_SECTOR vs FUND_AMT
plt.figure(figsize=(12, 7))
sns.boxplot(data=loan_df, x='INDUSTRY_SECTOR', y='FUND_AMT', palette='Set2')
plt.xlabel('Industry Sector', fontsize=12)
plt.ylabel('Fund Amount', fontsize=12)
plt.title('Bivariate: Industry Sector vs Fund Amount', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.ticklabel_format(style='plain', axis='y')
plt.tight_layout()
plt.show()

# Calculate median by industry
industry_median = loan_df.groupby('INDUSTRY_SECTOR')['FUND_AMT'].median().sort_values(ascending=False)
print(f'Median Fund Amount by Industry:\n{industry_median}')