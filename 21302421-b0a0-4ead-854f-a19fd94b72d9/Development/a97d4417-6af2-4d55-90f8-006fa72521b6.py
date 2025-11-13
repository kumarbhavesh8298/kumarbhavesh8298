import matplotlib.pyplot as plt
import numpy as np

# Create bar chart ranking features by missing percentage
features_with_missing = missing_summary_df[missing_summary_df['missing_pct'] > 0].sort_values('missing_pct', ascending=True)

fig, ax = plt.subplots(figsize=(10, 6))

_colors = ['red' if pct > 40 else 'orange' if pct > 20 else 'steelblue' 
           for pct in features_with_missing['missing_pct']]

ax.barh(features_with_missing['feature'], features_with_missing['missing_pct'], color=_colors)
ax.set_xlabel('Missing Percentage (%)', fontweight='bold')
ax.set_ylabel('Feature', fontweight='bold')
ax.set_title('Missing Data by Feature (Ranked)\nRed = >40%, Orange = >20%, Blue = <20%', 
             fontsize=11, fontweight='bold')
ax.axvline(x=40, color='red', linestyle='--', linewidth=1, alpha=0.7, label='40% threshold')
ax.legend()
ax.grid(axis='x', alpha=0.3)

plt.tight_layout()
plt.show()

print(f'Bar chart created with {len(features_with_missing)} features ranked by missingness')