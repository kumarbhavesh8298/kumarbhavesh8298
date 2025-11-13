import pandas as pd
import matplotlib.pyplot as plt

# Business and credit metrics for box plots
business_credit_metrics = [
    "BUSINESS_REVENUE", "BUSINESS_EXPENSES", "NET_PROFIT", 
    "CASH_FLOW", "OPERATING_PROFIT", "DEBT_TO_INCOME",
    "CREDIT_UTILIZATION", "PAYMENT_HISTORY_SCORE"
]

fig5, axes5 = plt.subplots(2, 4, figsize=(20, 10))
fig5.suptitle('Box Plots: Business & Credit Metrics (Outliers & Quartiles)', fontsize=16, y=0.995)
axes5 = axes5.flatten()

for _idx, _metric in enumerate(business_credit_metrics):
    ax = axes5[_idx]
    _data = loan_df[_metric].dropna()
    
    # Create box plot
    _box = ax.boxplot(_data, vert=True, patch_artist=True,
                       boxprops=dict(facecolor='lightgreen', alpha=0.7),
                       medianprops=dict(color='darkred', linewidth=2),
                       whiskerprops=dict(linewidth=1.5),
                       capprops=dict(linewidth=1.5),
                       flierprops=dict(marker='o', markerfacecolor='red', 
                                      markersize=4, alpha=0.5))
    
    # Add statistics as text
    _q1 = _data.quantile(0.25)
    _median = _data.median()
    _q3 = _data.quantile(0.75)
    _iqr = _q3 - _q1
    
    _stats_text = f'Q1: {_q1:.1f}\nMedian: {_median:.1f}\nQ3: {_q3:.1f}\nIQR: {_iqr:.1f}'
    ax.text(1.15, 0.5, _stats_text, transform=ax.transAxes,
            fontsize=8, verticalalignment='center',
            bbox=dict(boxstyle='round', facecolor='lightcyan', alpha=0.5))
    
    ax.set_title(f'{_metric}', fontsize=11, fontweight='bold')
    ax.set_ylabel('Value')
    ax.grid(axis='y', alpha=0.3)
    ax.set_xticklabels([''])

plt.tight_layout()
plt.show()

print(f'Created box plots for {len(business_credit_metrics)} business/credit metrics')