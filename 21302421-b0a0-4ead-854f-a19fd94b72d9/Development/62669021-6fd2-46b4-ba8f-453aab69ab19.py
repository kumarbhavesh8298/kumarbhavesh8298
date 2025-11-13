import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Create histograms with KDE overlay for all numeric features
numeric_cols = [
    "FUND_AMT", "BALANCE", "TOTAL_ASSETS", "TOTAL_LIABILITIES", 
    "ANNUAL_INCOME", "CREDIT_SCORE", "INTEREST_RATE", "COLLATERAL_VALUE",
    "BUSINESS_REVENUE", "BUSINESS_EXPENSES", "NET_PROFIT", 
    "CASH_FLOW", "OPERATING_PROFIT"
]

# Create multiple figures for better visualization
fig1, axes1 = plt.subplots(3, 3, figsize=(18, 14))
fig1.suptitle('Numeric Distributions: Financial Metrics (1/2)', fontsize=16, y=0.995)
axes1 = axes1.flatten()

for _idx, _col in enumerate(numeric_cols[:9]):
    ax = axes1[_idx]
    _data = loan_df[_col].dropna()
    
    # Histogram
    ax.hist(_data, bins=30, alpha=0.6, color='steelblue', edgecolor='black', density=True)
    
    # KDE overlay
    _kde_x = np.linspace(_data.min(), _data.max(), 100)
    _kde = stats.gaussian_kde(_data)
    ax.plot(_kde_x, _kde(_kde_x), 'r-', linewidth=2, label='KDE')
    
    ax.set_title(f'{_col}', fontsize=11, fontweight='bold')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.legend()
    ax.grid(alpha=0.3)

plt.tight_layout()
plt.show()

print(f'Created histogram+KDE plots for first 9 numeric features')