import pandas as pd

# Get object columns from imputed_df
obj_cols = imputed_df.select_dtypes(include=['object']).columns.tolist()

# Build list of dicts for cardinality info
cardinality_list = []
for colname in obj_cols:
    n_vals = imputed_df[colname].nunique()
    cardinality_list.append({
        'col': colname,
        'nunique': n_vals,
        'cat_type': 'HIGH' if n_vals > 10 else 'LOW'
    })

# Convert to DataFrame
cardinality_report = pd.DataFrame(cardinality_list).sort_values('nunique', ascending=False)

print('Categorical Feature Cardinality:')
for _, row in cardinality_report.iterrows():
    print(f"  {row['col']}: {row['nunique']} unique values ({row['cat_type']})")

# Split into high and low cardinality lists
high_cardinality_cols = cardinality_report[cardinality_report['cat_type'] == 'HIGH']['col'].tolist()
low_cardinality_cols = cardinality_report[cardinality_report['cat_type'] == 'LOW']['col'].tolist()

print(f'\nHigh cardinality features: {high_cardinality_cols}')
print(f'Low cardinality features: {low_cardinality_cols}')