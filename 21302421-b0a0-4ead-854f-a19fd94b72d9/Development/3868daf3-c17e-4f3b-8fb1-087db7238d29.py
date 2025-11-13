import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Integer/discrete columns that weren't covered yet
discrete_cols = [
    "CITY_TIER", "PREVIOUS_DEFAULTS", "TOTAL_PAID", "REMAINING_BALANCE"
]

fig6, axes6 = plt.subplots(2, 2, figsize=(16, 10))
fig6.suptitle('Additional Numeric Distributions', fontsize=16, y=0.995)
axes6 = axes6.flatten()

for _idx, _col in enumerate(discrete_cols):
    ax = axes6[_idx]
    
    if loan_df[_col].dtype in ['int64', 'int32']:
        # For integer columns, use bar chart
        _value_counts = loan_df[_col].value_counts().sort_index()
        ax.bar(_value_counts.index, _value_counts.values, 
               color='teal', edgecolor='black', alpha=0.7)
        ax.set_xlabel('Value')
        ax.set_ylabel('Frequency')
    else:
        # For continuous, use histogram
        _data = loan_df[_col].dropna()
        ax.hist(_data, bins=40, alpha=0.7, color='teal', edgecolor='black')
        ax.set_xlabel('Value')
        ax.set_ylabel('Frequency')
    
    ax.set_title(f'{_col}', fontsize=12, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

print(f'Created distribution plots for {len(discrete_cols)} additional features')