import pandas as pd
import numpy as np
from scipy import stats

# Identify MCAR/MAR/MNAR patterns using statistical tests
missingness_patterns = []

cols_with_missing = missing_summary_df[missing_summary_df['missing_pct'] > 0]['feature'].tolist()

# Test for each column with missing data
for _feature in cols_with_missing:
    _pattern_info = {
        'feature': _feature,
        'missing_pct': missing_summary_df[missing_summary_df['feature'] == _feature]['missing_pct'].values[0]
    }
    
    # Create missing indicator
    _is_missing = loan_df_with_missing[_feature].isnull()
    
    # Test relationship with categorical variables (chi-square test)
    _chi_sq_tests = []
    for _cat_col in ['LOAN_PURPOSE', 'EMPLOYMENT_STATUS', 'MARITAL_STATUS']:
        if _cat_col != _feature and loan_df_with_missing[_cat_col].notna().all():
            _contingency = pd.crosstab(_is_missing, loan_df_with_missing[_cat_col])
            _chi2, _p_val, _, _ = stats.chi2_contingency(_contingency)
            if _p_val < 0.05:
                _chi_sq_tests.append((_cat_col, _p_val))
    
    # Test relationship with numeric variables (t-test)
    _t_tests = []
    for _num_col in ['ANNUAL_INCOME', 'CREDIT_SCORE', 'LOAN_TERM']:
        if _num_col != _feature:
            _complete_vals = loan_df_with_missing[loan_df_with_missing[_feature].notna()][_num_col].dropna()
            _missing_vals = loan_df_with_missing[loan_df_with_missing[_feature].isna()][_num_col].dropna()
            if len(_complete_vals) > 0 and len(_missing_vals) > 0:
                _, _p_val = stats.ttest_ind(_complete_vals, _missing_vals, equal_var=False)
                if _p_val < 0.05:
                    _t_tests.append((_num_col, _p_val))
    
    # Classify missingness pattern
    if len(_chi_sq_tests) == 0 and len(_t_tests) == 0:
        _pattern_info['pattern'] = 'MCAR (Missing Completely At Random)'
        _pattern_info['reasoning'] = 'No significant relationships with other variables'
    elif len(_chi_sq_tests) > 0 or len(_t_tests) > 0:
        _pattern_info['pattern'] = 'MAR (Missing At Random)'
        _pattern_info['reasoning'] = f'Related to observed variables: {[t[0] for t in _chi_sq_tests + _t_tests]}'
    
    missingness_patterns.append(_pattern_info)

patterns_df = pd.DataFrame(missingness_patterns)

print(f'Statistical tests completed for {len(cols_with_missing)} features')
print(f'\\nPattern distribution:')
print(patterns_df['pattern'].value_counts())