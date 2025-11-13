import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Create binary missing data indicator matrix
missing_matrix = loan_df_with_missing.isnull().astype(int)

# Create heatmap showing missingness patterns by column
fig, ax = plt.subplots(figsize=(14, 10))

# Select only columns with missing data for visualization
cols_with_missing = missing_summary_df[missing_summary_df['missing_pct'] > 0]['feature'].tolist()
missing_subset = missing_matrix[cols_with_missing]

# Plot heatmap (showing first 100 rows for clarity)
sns.heatmap(missing_subset.head(100).T, cmap='RdYlGn_r', cbar_kws={'label': 'Missing (1) / Present (0)'}, 
            yticklabels=cols_with_missing, xticklabels=False, ax=ax)
ax.set_xlabel('Records (first 100 shown)')
ax.set_ylabel('Features')
ax.set_title('Missing Data Heatmap by Feature\n(Red = Missing, Green = Present)', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()

print(f'Heatmap created for {len(cols_with_missing)} features with missing data')