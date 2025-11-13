import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

# KNN imputation for correlated financial features
# The task mentions TOTAL_ASSETS, TOTAL_LIABILITIES, SHAREHOLDER_EQUITY
# Note: SHAREHOLDER_EQUITY doesn't exist, but we have TOTAL_ASSETS and TOTAL_LIABILITIES
# We'll also include CREDIT_SCORE and ANNUAL_INCOME (MCAR cols identified earlier)

knn_features = ['TOTAL_ASSETS', 'TOTAL_LIABILITIES', 'CREDIT_SCORE', 'ANNUAL_INCOME']

# Select features for KNN imputation (use related financial features as predictors)
knn_predictor_features = ['FUND_AMT', 'BALANCE', 'LOAN_TERM', 'INTEREST_RATE', 
                          'TOTAL_ASSETS', 'TOTAL_LIABILITIES', 'CREDIT_SCORE', 'ANNUAL_INCOME']

# Create a subset for KNN imputation
knn_df = imputed_df[knn_predictor_features].copy()

# Track which features actually have missing values
knn_features_with_missing = [f for f in knn_features if knn_df[f].isnull().sum() > 0]

if len(knn_features_with_missing) > 0:
    # Store pre-imputation state
    knn_imputed_count = {}
    for feature in knn_features_with_missing:
        knn_imputed_count[feature] = knn_df[feature].isnull().sum()
    
    # Apply KNN imputation (k=5 neighbors)
    knn_imputer = KNNImputer(n_neighbors=5, weights='distance')
    knn_df_imputed = pd.DataFrame(
        knn_imputer.fit_transform(knn_df),
        columns=knn_df.columns,
        index=knn_df.index
    )
    
    # Update the main imputed_df with KNN results
    for feature in knn_features_with_missing:
        imputed_df[feature] = knn_df_imputed[feature]
        # Create imputation flag
        imputed_df[f'{feature}_imputed_knn'] = loan_df_with_missing[feature].isnull().astype(int)
        print(f'{feature}: imputed {knn_imputed_count[feature]} values using KNN')
    
    print(f'\nKNN imputation completed for {len(knn_features_with_missing)} correlated financial features')
    print(f'Total values imputed: {sum(knn_imputed_count.values())}')
else:
    print('No correlated financial features with missing values found for KNN imputation')