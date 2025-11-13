import pandas as pd
import numpy as np

# Create derived risk indicators from financial ratios
risk_df = engineered_df.copy()

# 1. High Leverage Risk (leverage_ratio > 0.7 is concerning)
risk_df['high_leverage_risk'] = (risk_df['leverage_ratio'] > 0.7).astype(int)

# 2. Negative Profitability Risk
risk_df['negative_profit_risk'] = (risk_df['profit_margin'] < 0).astype(int)

# 3. Over-Utilization Risk (utilization > 0.9 means close to limit)
risk_df['over_utilization_risk'] = (risk_df['utilization_rate'] > 0.9).astype(int)

# 4. Under-Collateralized Risk (security_coverage < 1.0)
risk_df['under_collateralized_risk'] = (risk_df['security_coverage'] < 1.0).astype(int)

# 5. High Exposure Risk (exposure_intensity > 0.3)
risk_df['high_exposure_risk'] = (risk_df['exposure_intensity'] > 0.3).astype(int)

# 6. Low Equity Risk (equity_ratio < 0.2)
risk_df['low_equity_risk'] = (risk_df['equity_ratio'] < 0.2).astype(int)

# 7. Liquidity Risk (current_ratio < 1.5)
risk_df['liquidity_risk'] = (risk_df['current_ratio'] < 1.5).astype(int)

# 8. Composite Risk Score (sum of all binary risk indicators)
risk_indicators_cols = [
    'high_leverage_risk', 'negative_profit_risk', 'over_utilization_risk',
    'under_collateralized_risk', 'high_exposure_risk', 'low_equity_risk',
    'liquidity_risk'
]
risk_df['composite_risk_score'] = risk_df[risk_indicators_cols].sum(axis=1)

# 9. Risk Category (Low: 0-1, Medium: 2-3, High: 4-5, Critical: 6-7)
risk_df['risk_category'] = pd.cut(
    risk_df['composite_risk_score'],
    bins=[-1, 1, 3, 5, 7],
    labels=['Low', 'Medium', 'High', 'Critical']
)

print(f'Created 9 derived risk indicators')
print(f'Dataset shape: {risk_df.shape}')