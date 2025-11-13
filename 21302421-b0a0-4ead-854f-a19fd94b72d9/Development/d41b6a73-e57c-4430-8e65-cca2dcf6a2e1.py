import pandas as pd

# Get categorical columns
object_columns = imputed_df.select_dtypes(include=['object']).columns.tolist()

# Build cardinality info
info_list = []
for c in object_columns:
    u = imputed_df[c].nunique()
    info_list.append({'column': c, 'unique_count': u})

info_df = pd.DataFrame(info_list).sort_values('unique_count', ascending=False)

print('Categorical Features:')
print(info_df.to_string(index=False))

high_card = info_df[info_df['unique_count'] > 10]['column'].tolist()
low_card = info_df[info_df['unique_count'] <= 10]['column'].tolist()

print(f'\nHigh cardinality (>10): {high_card}')
print(f'Low cardinality (≤10): {low_card}')