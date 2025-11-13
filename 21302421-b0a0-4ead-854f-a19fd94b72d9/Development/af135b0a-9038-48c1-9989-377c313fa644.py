import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Create histograms with KDE overlay for remaining numeric features
numeric_cols_remaining = [
    "BUSINESS_REVENUE", "BUSINESS_EXPENSES", "NET_PROFIT", 
    "CASH_FLOW", "OPERATING_PROFIT"
]

# Additional numeric columns from the dataset
additional_numeric = [
    "LOAN_TERM", "YEARS_EMPLOYED", "DEBT_TO_INCOME", "NUM_DEPENDENTS",
    "CREDIT_HISTORY_LENGTH", "NUM_CREDIT_ACCOUNTS", "CREDIT_UTILIZATION",
    "NUM_RECENT_INQUIRIES", "PAYMENT_HISTORY_SCORE"
]

all_remaining_numeric = numeric_cols_remaining + additional_numeric

fig2, axes2 = plt.subplots(4, 4, figsize=(18, 16))
fig2.suptitle('Numeric Distributions: Additional Metrics (2/2)', fontsize=16, y=0.995)
axes2 = axes2.flatten()

for _idx, _col in enumerate(all_remaining_numeric):
    ax = axes2[_idx]
    _data = loan_df[_col].dropna()
    
    # Histogram
    ax.hist(_data, bins=30, alpha=0.6, color='steelblue', edgecolor='black', density=True)
    
    # KDE overlay
    _kde_x = np.linspace(_data.min(), _data.max(), 100)
    _kde = stats.gaussian_kde(_data)
    ax.plot(_kde_x, _kde(_kde_x), 'r-', linewidth=2, label='KDE')
    
    ax.set_title(f'{_col}', fontsize=10, fontweight='bold')
    ax.set_xlabel('Value', fontsize=9)
    ax.set_ylabel('Density', fontsize=9)
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

# Hide unused subplots
for _i in range(len(all_remaining_numeric), 16):
    fig2.delaxes(axes2[_i])

plt.tight_layout()
plt.show()

print(f'Created histogram+KDE plots for {len(all_remaining_numeric)} additional numeric features')