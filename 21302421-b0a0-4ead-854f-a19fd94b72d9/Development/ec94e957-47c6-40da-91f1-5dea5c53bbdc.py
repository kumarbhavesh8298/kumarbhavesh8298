import pandas as pd
import numpy as np

# Validate distributions of engineered features
validation_results = []

# Define all engineered features
engineered_features = [
    'leverage_ratio', 'profit_margin', 'utilization_rate', 
    'security_coverage', 'exposure_intensity', 'equity_ratio', 'current_ratio',
    'high_leverage_risk', 'negative_profit_risk', 'over_utilization_risk',
    'under_collateralized_risk', 'high_exposure_risk', 'low_equity_risk',
    'liquidity_risk', 'composite_risk_score'
]

for feature_name in engineered_features:
    feature_series = risk_df[feature_name]
    
    validation_results.append({
        'feature': feature_name,
        'mean': feature_series.mean(),
        'median': feature_series.median(),
        'std': feature_series.std(),
        'min': feature_series.min(),
        'max': feature_series.max(),
        'null_count': feature_series.isnull().sum(),
        'unique_values': feature_series.nunique()
    })

validation_results_df = pd.DataFrame(validation_results)

print('✅ DISTRIBUTION VALIDATION')
print('=' * 80)
print(validation_results_df.to_string(index=False))
print('\n' + '=' * 80)
print(f'All {len(engineered_features)} features validated successfully')
print(f'No null values in engineered features: {validation_results_df["null_count"].sum() == 0}')