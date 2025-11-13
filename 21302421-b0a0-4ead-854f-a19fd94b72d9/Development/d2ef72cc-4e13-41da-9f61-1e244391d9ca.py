import pandas as pd

# Profile categorical fields - unique values
categorical_cols = [
    'OCCP_CODE', 'INDUSTRY_SECTOR', 'MARITAL_STATUS', 
    'PAYMENT_FREQUENCY', 'LOAN_PURPOSE', 'EMPLOYMENT_STATUS',
    'EDUCATION_LEVEL', 'HOME_OWNERSHIP', 'REGION', 'LOAN_STATUS'
]

print("=" * 50)
print("CATEGORICAL FIELDS PROFILE")
print("=" * 50)

for cat_col in categorical_cols:
    unique_vals = loan_df[cat_col].nunique()
    top_values = loan_df[cat_col].value_counts().head(3)
    
    print(f"\n{cat_col}:")
    print(f"  Unique Values: {unique_vals}")
    print(f"  Top 3:")
    for val, count in top_values.items():
        print(f"    {val}: {count} ({count/len(loan_df)*100:.1f}%)")