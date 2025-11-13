import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

# Select key features for segmentation
pcoord_features = ['CREDIT_SCORE', 'ANNUAL_INCOME', 'DEBT_TO_INCOME', 'CREDIT_UTILIZATION', 'PAYMENT_HISTORY_SCORE', 'LOAN_STATUS']
pcoord_df = imputed_df[pcoord_features].copy()

# Normalize numeric columns to 0-1 scale
for _pcol in ['CREDIT_SCORE', 'ANNUAL_INCOME', 'DEBT_TO_INCOME', 'CREDIT_UTILIZATION', 'PAYMENT_HISTORY_SCORE']:
    _pmin = pcoord_df[_pcol].min()
    _pmax = pcoord_df[_pcol].max()
    pcoord_df[_pcol] = (pcoord_df[_pcol] - _pmin) / (_pmax - _pmin)

# Sample for better visualization
pcoord_sample = pcoord_df.sample(n=min(300, len(pcoord_df)), random_state=42)

plt.figure(figsize=(16, 8))
parallel_coordinates(pcoord_sample, 'LOAN_STATUS', colormap='viridis', alpha=0.6)
plt.title('Parallel Coordinates: Multi-dimensional Customer Segments by Loan Status', fontsize=14, fontweight='bold')
plt.xlabel('Features (Normalized)', fontsize=12)
plt.ylabel('Normalized Values', fontsize=12)
plt.legend(title='Loan Status', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45, ha='right')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

print(f'Parallel coordinates: {len(pcoord_sample)} samples, {len(pcoord_sample["LOAN_STATUS"].unique())} loan statuses')