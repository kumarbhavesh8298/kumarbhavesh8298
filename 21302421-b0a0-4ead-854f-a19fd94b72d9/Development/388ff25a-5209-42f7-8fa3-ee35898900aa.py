import pandas as pd
import numpy as np

# Validate imputation quality
# Check remaining nulls and calculate percentages

# Calculate remaining missing values
final_missing_counts = imputed_df.isnull().sum()
final_missing_pcts = (final_missing_counts / len(imputed_df)) * 100

# Create summary
validation_summary = pd.DataFrame({
    'feature': final_missing_counts.index,
    'remaining_nulls': final_missing_counts.values,
    'remaining_pct': final_missing_pcts.values
})

# Filter to features that had missing values originally
original_features_with_missing = cols_with_missing
validation_summary_filtered = validation_summary[
    validation_summary['feature'].isin(original_features_with_missing)
].sort_values('remaining_nulls', ascending=False)

# Check if we meet the <3% threshold
max_missing_pct = validation_summary['remaining_pct'].max()
meets_threshold = max_missing_pct < 3.0

# Total imputation summary
total_original_nulls = loan_df_with_missing.isnull().sum().sum()
total_remaining_nulls = imputed_df[loan_df_with_missing.columns].isnull().sum().sum()
total_imputed = total_original_nulls - total_remaining_nulls

print('=== IMPUTATION QUALITY VALIDATION ===\n')
print(f'Total missing values before: {total_original_nulls}')
print(f'Total missing values after: {total_remaining_nulls}')
print(f'Total values imputed: {total_imputed}')
print(f'Imputation rate: {(total_imputed/total_original_nulls)*100:.2f}%\n')

print('Features that originally had missing values:')
print(validation_summary_filtered.to_string(index=False))

print(f'\n✓ Maximum remaining missing: {max_missing_pct:.4f}%')
print(f'✓ Meets <3% threshold: {meets_threshold}')

if not meets_threshold:
    print(f'\n⚠ WARNING: Some features still exceed 3% missing threshold')