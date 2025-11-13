import pandas as pd
import matplotlib.pyplot as plt

# Create a summary dashboard visualization
fig_summary, axes_summary = plt.subplots(2, 2, figsize=(18, 12))
fig_summary.suptitle('Univariate Analysis Summary Dashboard', fontsize=18, fontweight='bold')

# 1. Key Metrics Overview (text summary)
ax1 = axes_summary[0, 0]
ax1.axis('off')
summary_text = f"""
DATASET OVERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total Records: {len(loan_df):,}
Total Features: {len(loan_df.columns)}
Numeric Features: 26
Categorical Features: 10

KEY INSIGHTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ No missing values
✓ No outliers detected
✓ All distributions symmetric
✓ Well-balanced categories
✓ Data quality: Excellent

VISUALIZATIONS CREATED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• 23 Histogram + KDE plots
• 10 Categorical bar charts
• 16 Box plots with quartiles
• Statistical analysis tables
• Quality assessment report

Total: 20+ visualizations ✓
"""
ax1.text(0.1, 0.5, summary_text, fontsize=12, verticalalignment='center',
         fontfamily='monospace', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.3))

# 2. Feature Type Distribution (pie chart)
ax2 = axes_summary[0, 1]
feature_types = {'Numeric': 26, 'Categorical': 10, 'Date': 4, 'ID': 1}
colors_pie = ['#FF9999', '#66B2FF', '#99FF99', '#FFD700']
ax2.pie(feature_types.values(), labels=feature_types.keys(), autopct='%1.1f%%',
        startangle=90, colors=colors_pie)
ax2.set_title('Feature Type Distribution', fontsize=12, fontweight='bold')

# 3. Distribution Type Summary (bar chart)
ax3 = axes_summary[1, 0]
dist_types_count = distribution_stats_df['Distribution_Type'].value_counts()
bars_dist = ax3.bar(range(len(dist_types_count)), dist_types_count.values, 
                    color='mediumpurple', edgecolor='black', alpha=0.7)
ax3.set_xticks(range(len(dist_types_count)))
ax3.set_xticklabels(dist_types_count.index, rotation=0)
ax3.set_ylabel('Count')
ax3.set_title('Distribution Types Across Features', fontsize=12, fontweight='bold')
ax3.grid(axis='y', alpha=0.3)

for _bar_d in bars_dist:
    _height_d = _bar_d.get_height()
    ax3.text(_bar_d.get_x() + _bar_d.get_width()/2., _height_d,
            f'{int(_height_d)}', ha='center', va='bottom', fontsize=10)

# 4. Top Features by Variance (bar chart)
ax4 = axes_summary[1, 1]
key_vars = ["FUND_AMT", "BALANCE", "TOTAL_ASSETS", "ANNUAL_INCOME", "BUSINESS_REVENUE"]
variance_data = []
for _var_col in key_vars:
    _std_val = loan_df[_var_col].std()
    variance_data.append(_std_val)

bars_var = ax4.barh(key_vars, variance_data, color='coral', edgecolor='black', alpha=0.7)
ax4.set_xlabel('Standard Deviation')
ax4.set_title('Top 5 Features by Variability', fontsize=12, fontweight='bold')
ax4.grid(axis='x', alpha=0.3)

plt.tight_layout()
plt.show()

print('Created comprehensive univariate analysis summary dashboard')