import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

p1_features = ['CREDIT_SCORE', 'ANNUAL_INCOME', 'DEBT_TO_INCOME', 'CREDIT_UTILIZATION', 'PAYMENT_HISTORY_SCORE', 'LOAN_STATUS']
p1_df = imputed_df[p1_features].copy()

for p1_col in ['CREDIT_SCORE', 'ANNUAL_INCOME', 'DEBT_TO_INCOME', 'CREDIT_UTILIZATION', 'PAYMENT_HISTORY_SCORE']:
    p1_min = p1_df[p1_col].min()
    p1_max = p1_df[p1_col].max()
    p1_df[p1_col] = (p1_df[p1_col] - p1_min) / (p1_max - p1_min)

p1_sample = p1_df.sample(n=min(300, len(p1_df)), random_state=42)

plt.figure(figsize=(16, 8))
parallel_coordinates(p1_sample, 'LOAN_STATUS', colormap='viridis', alpha=0.6)
plt.title('1. Parallel Coordinates: Multi-dimensional Customer Segments', fontsize=14, fontweight='bold')
plt.xlabel('Features', fontsize=12)
plt.ylabel('Normalized Values', fontsize=12)
plt.legend(title='Loan Status', bbox_to_anchor=(1.05, 1))
plt.xticks(rotation=45, ha='right')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

print(f'Parallel coordinates: {len(p1_sample)} samples')