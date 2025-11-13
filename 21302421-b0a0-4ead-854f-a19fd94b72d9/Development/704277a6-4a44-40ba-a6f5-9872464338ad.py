import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

# Parallel coordinates: multi-dimensional customer segmentation
v1_cols = ['CREDIT_SCORE', 'ANNUAL_INCOME', 'DEBT_TO_INCOME', 'CREDIT_UTILIZATION', 'PAYMENT_HISTORY_SCORE', 'LOAN_STATUS']
v1_df = imputed_df[v1_cols].copy()

# Normalize to 0-1
for _c1 in ['CREDIT_SCORE', 'ANNUAL_INCOME', 'DEBT_TO_INCOME', 'CREDIT_UTILIZATION', 'PAYMENT_HISTORY_SCORE']:
    _min1 = v1_df[_c1].min()
    _max1 = v1_df[_c1].max()
    v1_df[_c1] = (v1_df[_c1] - _min1) / (_max1 - _min1)

v1_sample = v1_df.sample(n=min(300, len(v1_df)), random_state=42)

plt.figure(figsize=(16, 8))
parallel_coordinates(v1_sample, 'LOAN_STATUS', colormap='viridis', alpha=0.6)
plt.title('1. Parallel Coordinates: Multi-dimensional Customer Segments', fontsize=14, fontweight='bold')
plt.xlabel('Features', fontsize=12)
plt.ylabel('Normalized Values', fontsize=12)
plt.legend(title='Loan Status', bbox_to_anchor=(1.05, 1))
plt.xticks(rotation=45, ha='right')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

print(f'Parallel coordinates: {len(v1_sample)} samples')