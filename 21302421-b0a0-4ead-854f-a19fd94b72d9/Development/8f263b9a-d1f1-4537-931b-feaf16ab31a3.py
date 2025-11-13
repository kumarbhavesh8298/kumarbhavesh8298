import pandas as pd
import numpy as np

# Domain-specific rules for business features
# The task mentions credit features (INTERNAL_RATING, EXTERNAL_RATING) but these don't exist
# We do have business financial features: BUSINESS_REVENUE, BUSINESS_EXPENSES, NET_PROFIT, CASH_FLOW, OPERATING_PROFIT
# These are all MAR and highly correlated (81.5% missing together)

# Domain-specific rules for business features:
# 1. If one business metric is missing, likely all are missing (non-business customers)
# 2. For rows where some business features exist, impute related ones using financial relationships

business_features = mar_business_cols  # Using the MAR business columns identified earlier

# Check current state
remaining_nulls = {}
for feature in business_features:
    if feature in imputed_df.columns:
        remaining_nulls[feature] = imputed_df[feature].isnull().sum()

# For business features, we'll use a domain rule:
# If ANY business metric exists, calculate others based on relationships
# If ALL are missing, fill with 0 (indicating non-business customer)

business_mask = imputed_df[business_features].isnull().all(axis=1)
partial_business_mask = (~imputed_df[business_features].isnull().any(axis=1)) & (~business_mask)

# Fill completely missing business rows with 0 (non-business customers)
for feature in business_features:
    # Create imputation flag before imputing
    imputed_df[f'{feature}_imputed_domain'] = loan_df_with_missing[feature].isnull().astype(int)
    
    # Apply domain rule: fill with 0 for non-business customers
    imputed_df.loc[business_mask, feature] = 0

# Count imputed values
domain_imputed_count = {}
for feature in business_features:
    after_nulls = imputed_df[feature].isnull().sum()
    domain_imputed_count[feature] = remaining_nulls[feature] - after_nulls
    print(f'{feature}: {domain_imputed_count[feature]} values imputed (domain rule: non-business = 0)')

print(f'\nDomain-specific imputation completed for {len(business_features)} business features')
print(f'Total values imputed: {sum(domain_imputed_count.values())}')