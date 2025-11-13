import pandas as pd
import matplotlib.pyplot as plt

# Key financial metrics for box plots
financial_metrics = [
    "FUND_AMT", "BALANCE", "TOTAL_ASSETS", "TOTAL_LIABILITIES",
    "ANNUAL_INCOME", "CREDIT_SCORE", "INTEREST_RATE", "COLLATERAL_VALUE"
]

fig4, axes4 = plt.subplots(2, 4, figsize=(20, 10))
fig4.suptitle('Box Plots: Key Financial Metrics (Outliers & Quartiles)', fontsize=16, y=0.995)
axes4 = axes4.flatten()

for _idx, _metric in enumerate(financial_metrics):
    ax = axes4[_idx]
    _data = loan_df[_metric].dropna()
    
    # Create box plot
    _box = ax.boxplot(_data, vert=True, patch_artist=True,
                       boxprops=dict(facecolor='lightblue', alpha=0.7),
                       medianprops=dict(color='red', linewidth=2),
                       whiskerprops=dict(linewidth=1.5),
                       capprops=dict(linewidth=1.5),
                       flierprops=dict(marker='o', markerfacecolor='red', 
                                      markersize=4, alpha=0.5))
    
    # Add statistics as text
    _q1 = _data.quantile(0.25)
    _median = _data.median()
    _q3 = _data.quantile(0.75)
    _iqr = _q3 - _q1
    
    _stats_text = f'Q1: {_q1:.0f}\nMedian: {_median:.0f}\nQ3: {_q3:.0f}\nIQR: {_iqr:.0f}'
    ax.text(1.15, 0.5, _stats_text, transform=ax.transAxes,
            fontsize=8, verticalalignment='center',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    ax.set_title(f'{_metric}', fontsize=11, fontweight='bold')
    ax.set_ylabel('Value')
    ax.grid(axis='y', alpha=0.3)
    ax.set_xticklabels([''])

plt.tight_layout()
plt.show()

print(f'Created box plots for {len(financial_metrics)} financial metrics')