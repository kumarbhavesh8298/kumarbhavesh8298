import matplotlib.pyplot as plt
import numpy as np

# Visualize distributions of financial ratios
financial_ratios = [
    'leverage_ratio', 'profit_margin', 'utilization_rate', 
    'security_coverage', 'exposure_intensity', 'equity_ratio', 'current_ratio'
]

fig_dist, axes_dist = plt.subplots(3, 3, figsize=(15, 12))
axes_dist = axes_dist.flatten()

for idx, ratio_col in enumerate(financial_ratios):
    ax_dist = axes_dist[idx]
    
    # Plot histogram with log scale for better visualization
    ratio_data = risk_df[ratio_col]
    ax_dist.hist(ratio_data, bins=50, edgecolor='black', alpha=0.7)
    ax_dist.set_title(f'{ratio_col}\n(mean={ratio_data.mean():.2f}, median={ratio_data.median():.2f})')
    ax_dist.set_xlabel('Value')
    ax_dist.set_ylabel('Frequency')
    ax_dist.grid(True, alpha=0.3)

# Remove empty subplots
for idx in range(len(financial_ratios), len(axes_dist)):
    fig_dist.delaxes(axes_dist[idx])

plt.tight_layout()
plt.show()

print('✅ Financial ratio distributions plotted')