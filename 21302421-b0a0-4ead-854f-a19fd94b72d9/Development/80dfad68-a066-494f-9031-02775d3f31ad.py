import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create correlation matrix for all numeric features
numeric_cols = loan_df.select_dtypes(include=[np.number]).columns.tolist()
correlation_matrix = loan_df[numeric_cols].corr()

# Create heatmap
plt.figure(figsize=(16, 14))
sns.heatmap(correlation_matrix, annot=False, cmap='coolwarm', center=0, 
            linewidths=0.5, cbar_kws={'label': 'Correlation'})
plt.title('Correlation Heatmap: All Numeric Features', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

# Identify strongest correlations (excluding diagonal)
corr_pairs = []
for i in range(len(correlation_matrix.columns)):
    for j in range(i+1, len(correlation_matrix.columns)):
        corr_pairs.append({
            'feature1': correlation_matrix.columns[i],
            'feature2': correlation_matrix.columns[j],
            'correlation': correlation_matrix.iloc[i, j]
        })

top_correlations = pd.DataFrame(corr_pairs).sort_values('correlation', key=abs, ascending=False).head(10)
print(f'Top 10 strongest correlations:\n{top_correlations.to_string(index=False)}')