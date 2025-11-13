import pandas as pd
import numpy as np

# Before/After Statistics Comparison
numeric_features = loan_df_with_missing.select_dtypes(include=[np.number]).columns.tolist()

before_stats = loan_df_with_missing[numeric_features].describe().T
after_stats = imputed_df[numeric_features].describe().T

# Focus on features that had missing values
features_to_compare = cols_with_missing

stats_comparison_table = pd.DataFrame({
    'Feature': features_to_compare,
    'Before_Mean': [before_stats.loc[f, 'mean'] for f in features_to_compare],
    'After_Mean': [after_stats.loc[f, 'mean'] for f in features_to_compare],
    'Before_Std': [before_stats.loc[f, 'std'] for f in features_to_compare],
    'After_Std': [after_stats.loc[f, 'std'] for f in features_to_compare],
    'Missing_Before': [loan_df_with_missing[f].isnull().sum() for f in features_to_compare],
    'Missing_After': [imputed_df[f].isnull().sum() for f in features_to_compare]
})

stats_comparison_table['Mean_Change%'] = ((stats_comparison_table['After_Mean'] - stats_comparison_table['Before_Mean']) / stats_comparison_table['Before_Mean'].abs()) * 100
stats_comparison_table['Std_Change%'] = ((stats_comparison_table['After_Std'] - stats_comparison_table['Before_Std']) / stats_comparison_table['Before_Std']) * 100

print('BEFORE/AFTER STATISTICS COMPARISON')
print(stats_comparison_table.round(3).to_string(index=False))