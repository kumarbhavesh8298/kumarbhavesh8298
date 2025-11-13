import pandas as pd
import numpy as np

# Create financial health feature engineering
# Based on available columns in imputed_df
engineered_df = imputed_df.copy()

# 1. LEVERAGE_RATIO = TOTAL_LIABILITIES / TOTAL_ASSETS
# Measures financial leverage - higher means more debt-dependent
engineered_df['leverage_ratio'] = np.where(
    engineered_df['TOTAL_ASSETS'] != 0,
    engineered_df['TOTAL_LIABILITIES'] / engineered_df['TOTAL_ASSETS'],
    0
)

# 2. PROFIT_MARGIN = OPERATING_PROFIT / ANNUAL_REVENUE
# Note: Using ANNUAL_INCOME as proxy for revenue for non-business customers
# For business customers, using BUSINESS_REVENUE
engineered_df['revenue_proxy'] = np.where(
    engineered_df['BUSINESS_REVENUE'] > 0,
    engineered_df['BUSINESS_REVENUE'],
    engineered_df['ANNUAL_INCOME']
)
engineered_df['profit_margin'] = np.where(
    engineered_df['revenue_proxy'] != 0,
    engineered_df['OPERATING_PROFIT'] / engineered_df['revenue_proxy'],
    0
)

# 3. UTILIZATION_RATE = BALANCE / CURRENT_SANCTION_LIMIT
# Note: CURRENT_SANCTION_LIMIT not in dataset, using FUND_AMT as sanctioned amount
engineered_df['utilization_rate'] = np.where(
    engineered_df['FUND_AMT'] != 0,
    engineered_df['BALANCE'] / engineered_df['FUND_AMT'],
    0
)

# 4. SECURITY_COVERAGE = A_PRIMARY_SECURITY_VALUE / FUND_AMT
# Using COLLATERAL_VALUE as primary security value
engineered_df['security_coverage'] = np.where(
    engineered_df['FUND_AMT'] != 0,
    engineered_df['COLLATERAL_VALUE'] / engineered_df['FUND_AMT'],
    0
)

# 5. EXPOSURE_INTENSITY = TOTAL_CR_EXP / TOTAL_ASSETS
# Using BALANCE as total credit exposure
engineered_df['exposure_intensity'] = np.where(
    engineered_df['TOTAL_ASSETS'] != 0,
    engineered_df['BALANCE'] / engineered_df['TOTAL_ASSETS'],
    0
)

# 6. EQUITY_RATIO = SHAREHOLDER_EQUITY / TOTAL_ASSETS
# Shareholder equity = TOTAL_ASSETS - TOTAL_LIABILITIES
engineered_df['shareholder_equity'] = engineered_df['TOTAL_ASSETS'] - engineered_df['TOTAL_LIABILITIES']
engineered_df['equity_ratio'] = np.where(
    engineered_df['TOTAL_ASSETS'] != 0,
    engineered_df['shareholder_equity'] / engineered_df['TOTAL_ASSETS'],
    0
)

# 7. CURRENT_RATIO approximation
# Using TOTAL_ASSETS as proxy for current assets and BALANCE as current liabilities proxy
engineered_df['current_ratio'] = np.where(
    engineered_df['BALANCE'] != 0,
    engineered_df['TOTAL_ASSETS'] / engineered_df['BALANCE'],
    0
)

print(f'Created 7 core financial ratios')
print(f'Dataset shape: {engineered_df.shape}')