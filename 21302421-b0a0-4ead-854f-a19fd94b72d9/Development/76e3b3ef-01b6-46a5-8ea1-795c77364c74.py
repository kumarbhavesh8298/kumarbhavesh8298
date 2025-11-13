import matplotlib.pyplot as plt

# Visualize risk category distribution
risk_category_counts = risk_df['risk_category'].value_counts().sort_index()

fig_risk, ax_risk = plt.subplots(figsize=(10, 6))
risk_category_counts.plot(kind='bar', ax=ax_risk, color=['green', 'yellow', 'orange', 'red'])
ax_risk.set_title('Risk Category Distribution', fontsize=14, fontweight='bold')
ax_risk.set_xlabel('Risk Category')
ax_risk.set_ylabel('Number of Customers')
ax_risk.grid(True, alpha=0.3, axis='y')

for idx_bar, val_bar in enumerate(risk_category_counts):
    ax_risk.text(idx_bar, val_bar + 5, str(val_bar), ha='center', fontweight='bold')

plt.tight_layout()
plt.show()

print(f'Risk Category Distribution:')
for cat_name, cat_count in risk_category_counts.items():
    print(f'  {cat_name}: {cat_count} ({cat_count/len(risk_df)*100:.1f}%)')