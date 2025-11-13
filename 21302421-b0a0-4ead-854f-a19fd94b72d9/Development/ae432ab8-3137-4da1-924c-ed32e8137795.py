import pandas as pd

# Identify categorical columns
cat_list = imputed_df.select_dtypes(include=['object']).columns.tolist()

# Analyze cardinality
results = []
for c in cat_list:
    nuniq = imputed_df[c].nunique()
    results.append({'feature': c, 'n_unique': nuniq, 'type': 'high' if nuniq > 10 else 'low'})

card_df = pd.DataFrame(results).sort_values('n_unique', ascending=False)

print('Categorical Cardinality:')
print(card_df.to_string(index=False))

high_card_list = card_df[card_df['type'] == 'high']['feature'].tolist()
low_card_list = card_df[card_df['type'] == 'low']['feature'].tolist()

print(f'\nHigh (>10): {high_card_list}')
print(f'Low (≤10): {low_card_list}')