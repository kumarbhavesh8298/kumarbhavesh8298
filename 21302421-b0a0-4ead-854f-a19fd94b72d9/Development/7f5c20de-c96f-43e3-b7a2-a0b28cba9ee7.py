import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

# Parallel coordinates for multi-dimensional customer segments
viz1_features = ['CREDIT_SCORE', 'ANNUAL_INCOME', 'DEBT_TO_INCOME', 'CREDIT_UTILIZATION', 'PAYMENT_HISTORY_SCORE', 'LOAN_STATUS']
viz1_data = imputed_df[viz1_features].copy()

# Normalize numeric columns
for _v1c in ['CREDIT_SCORE', 'ANNUAL_INCOME', 'DEBT_TO_INCOME', 'CREDIT_UTILIZATION', 'PAYMENT_HISTORY_SCORE']:
    _v1min = viz1_data[_v1c].min()
    _v1max = viz1_data[_v1c].max()
    viz1_data[_v1c] = (viz1_data[_v1c] - _v1min) / (_v1max - _v1min)

# Sample rows
viz1_sample = viz1_data.sample(n=min(300, len(viz1_data)), random_state=42)

plt.figure(figsize=(16, 8))
parallel_coordinates(viz1_sample, 'LOAN_STATUS', colormap='viridis', alpha=0.6)
plt.title('Parallel Coordinates: Multi-dimensional Customer Segments', fontsize=14, fontweight='bold')
plt.xlabel('Features', fontsize=12)
plt.ylabel('Normalized Values', fontsize=12)
plt.legend(title='Loan Status', bbox_to_anchor=(1.05, 1))
plt.xticks(rotation=45, ha='right')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

print(f'Viz 1: Parallel coordinates with {len(viz1_sample)} samples')