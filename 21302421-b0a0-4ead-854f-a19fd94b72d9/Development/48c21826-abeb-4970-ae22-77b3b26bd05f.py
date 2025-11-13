import pandas as pd

# Count and summarize all engineered features
# Core financial ratios
financial_ratio_cols = [
    'leverage_ratio', 'profit_margin', 'utilization_rate', 
    'security_coverage', 'exposure_intensity', 'equity_ratio', 'current_ratio'
]

# Intermediate features
intermediate_cols = ['revenue_proxy', 'shareholder_equity']

# Risk indicators
risk_indicator_cols = [
    'high_leverage_risk', 'negative_profit_risk', 'over_utilization_risk',
    'under_collateralized_risk', 'high_exposure_risk', 'low_equity_risk',
    'liquidity_risk', 'composite_risk_score', 'risk_category'
]

# Total engineered features
all_engineered_features = financial_ratio_cols + intermediate_cols + risk_indicator_cols

print(f'📊 FEATURE ENGINEERING SUMMARY')
print(f'=' * 50)
print(f'Core Financial Ratios: {len(financial_ratio_cols)}')
for feat_col in financial_ratio_cols:
    print(f'  - {feat_col}')

print(f'\nIntermediate Features: {len(intermediate_cols)}')
for feat_col in intermediate_cols:
    print(f'  - {feat_col}')

print(f'\nRisk Indicators: {len(risk_indicator_cols)}')
for feat_col in risk_indicator_cols:
    print(f'  - {feat_col}')

print(f'\n' + '=' * 50)
print(f'Total Engineered Features: {len(all_engineered_features)}')
print(f'Final Dataset Shape: {risk_df.shape}')
print(f'New Features Added: {risk_df.shape[1] - imputed_df.shape[1]}')