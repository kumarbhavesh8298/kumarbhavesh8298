import pandas as pd

# Generate comprehensive missing data report with imputation recommendations
report_data = []

for _, row in patterns_df.iterrows():
    _feature = row['feature']
    _missing_pct = row['missing_pct']
    _pattern = row['pattern']
    _reasoning = row['reasoning']
    
    # Determine imputation strategy based on pattern and percentage
    if _missing_pct > 40:
        _strategy = 'DROP or BUSINESS_RULE'
        _recommendation = 'Consider dropping or using domain-specific rules (>40% missing)'
    elif 'MAR' in _pattern:
        if _missing_pct > 20:
            _strategy = 'MULTIPLE_IMPUTATION or MODEL_BASED'
            _recommendation = 'Use multiple imputation (MICE) or predictive modeling based on related variables'
        else:
            _strategy = 'MEAN/MEDIAN or KNN'
            _recommendation = 'Use mean/median imputation or KNN based on similar records'
    elif 'MCAR' in _pattern:
        _strategy = 'MEAN/MEDIAN or MODE'
        _recommendation = 'Simple imputation (mean/median for numeric, mode for categorical)'
    else:
        _strategy = 'DOMAIN_SPECIFIC'
        _recommendation = 'Requires domain expertise - potential MNAR pattern'
    
    report_data.append({
        'feature': _feature,
        'missing_pct': round(_missing_pct, 2),
        'missing_count': missing_summary_df[missing_summary_df['feature'] == _feature]['missing_count'].values[0],
        'pattern': _pattern,
        'reasoning': _reasoning,
        'imputation_strategy': _strategy,
        'recommendation': _recommendation
    })

comprehensive_report_df = pd.DataFrame(report_data).sort_values('missing_pct', ascending=False)

print('=' * 80)
print('COMPREHENSIVE MISSING DATA ANALYSIS REPORT')
print('=' * 80)
print(f'\\nTotal features analyzed: {len(loan_df_with_missing.columns)}')
print(f'Features with missing data: {len(comprehensive_report_df)}')
print(f'Features with >40% missing (HIGH RISK): {len(high_miss_features)}')
print(f'\\nHigh missingness features: {high_miss_features}')
print('\\n' + '=' * 80)
print(comprehensive_report_df.to_string(index=False))
print('=' * 80)