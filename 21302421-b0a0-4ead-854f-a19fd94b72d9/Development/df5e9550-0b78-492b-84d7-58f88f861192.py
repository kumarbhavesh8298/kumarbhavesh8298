import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

# Parallel coordinates
cols1 = ['CREDIT_SCORE', 'ANNUAL_INCOME', 'DEBT_TO_INCOME', 'CREDIT_UTILIZATION', 'PAYMENT_HISTORY_SCORE', 'LOAN_STATUS']
df1 = imputed_df[cols1].copy()

# Normalize
for c in ['CREDIT_SCORE', 'ANNUAL_INCOME', 'DEBT_TO_INCOME', 'CREDIT_UTILIZATION', 'PAYMENT_HISTORY_SCORE']:
    mn = df1[c].min()
    mx = df1[c].max()
    df1[c] = (df1[c] - mn) / (mx - mn)

sample1 = df1.sample(n=min(300, len(df1)), random_state=42)

plt.figure(figsize=(16, 8))
parallel_coordinates(sample1, 'LOAN_STATUS', colormap='viridis', alpha=0.6)
plt.title('1. Parallel Coordinates: Customer Segments', fontsize=14, fontweight='bold')
plt.xlabel('Features', fontsize=12)
plt.ylabel('Values', fontsize=12)
plt.legend(title='Loan Status', bbox_to_anchor=(1.05, 1))
plt.xticks(rotation=45)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

print(f'Parallel coords: {len(sample1)} samples')