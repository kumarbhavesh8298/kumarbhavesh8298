import pandas as pd
import matplotlib.pyplot as plt

# Categorical columns for bar charts
categorical_cols = [
    "OCCP_CODE", "INDUSTRY_SECTOR", "MARITAL_STATUS", 
    "PAYMENT_FREQUENCY", "LOAN_PURPOSE", "EMPLOYMENT_STATUS",
    "EDUCATION_LEVEL", "HOME_OWNERSHIP", "REGION", "LOAN_STATUS"
]

fig3, axes3 = plt.subplots(3, 4, figsize=(20, 12))
fig3.suptitle('Categorical Distributions', fontsize=16, y=0.995)
axes3 = axes3.flatten()

for _idx, _cat_col in enumerate(categorical_cols):
    ax = axes3[_idx]
    _value_counts = loan_df[_cat_col].value_counts()
    
    # Create bar chart
    _bars = ax.bar(_value_counts.index, _value_counts.values, 
                    color='coral', edgecolor='black', alpha=0.7)
    
    # Add value labels on bars
    for _bar in _bars:
        _height = _bar.get_height()
        ax.text(_bar.get_x() + _bar.get_width()/2., _height,
                f'{int(_height)}',
                ha='center', va='bottom', fontsize=8)
    
    ax.set_title(f'{_cat_col}', fontsize=11, fontweight='bold')
    ax.set_xlabel('Category', fontsize=9)
    ax.set_ylabel('Count', fontsize=9)
    ax.tick_params(axis='x', rotation=45, labelsize=8)
    ax.grid(axis='y', alpha=0.3)

# Hide unused subplots
for _i in range(len(categorical_cols), 12):
    fig3.delaxes(axes3[_i])

plt.tight_layout()
plt.show()

print(f'Created bar charts for {len(categorical_cols)} categorical features')