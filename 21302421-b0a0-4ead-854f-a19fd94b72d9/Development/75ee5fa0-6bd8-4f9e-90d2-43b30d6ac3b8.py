import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Box plot: REGION vs BALANCE
plt.figure(figsize=(12, 7))
sns.boxplot(data=loan_df, x='REGION', y='BALANCE', palette='Set3')
plt.xlabel('Region', fontsize=12)
plt.ylabel('Current Balance', fontsize=12)
plt.title('Bivariate: Region vs Balance', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.ticklabel_format(style='plain', axis='y')
plt.tight_layout()
plt.show()

# Calculate statistics by region
region_stats = loan_df.groupby('REGION')['BALANCE'].agg(['mean', 'median', 'std']).round(2)
print(f'Balance statistics by Region:\n{region_stats}')