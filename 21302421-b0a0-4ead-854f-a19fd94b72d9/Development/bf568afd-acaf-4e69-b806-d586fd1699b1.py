import matplotlib.pyplot as plt
import seaborn as sns

# Calculate correlations between missing indicators
missing_indicators = loan_df_with_missing.isnull().astype(int)
cols_with_missing = missing_summary_df[missing_summary_df['missing_pct'] > 0]['feature'].tolist()
missing_corr = missing_indicators[cols_with_missing].corr()

# Create correlation heatmap
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(missing_corr, annot=True, fmt='.2f', cmap='coolwarm', center=0,
            square=True, linewidths=1, cbar_kws={'label': 'Correlation'}, ax=ax)
ax.set_title('Correlation Between Missing Data Indicators\n(Shows which features tend to be missing together)', 
             fontsize=11, fontweight='bold')
plt.tight_layout()
plt.show()

print(f'Correlation heatmap created for {len(cols_with_missing)} features')