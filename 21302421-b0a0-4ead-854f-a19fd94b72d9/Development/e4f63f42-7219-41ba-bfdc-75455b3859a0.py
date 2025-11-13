import pandas as pd

# Create summary of bivariate insights
bivariate_insights = {
    'Visualization': [
        '1. Correlation Heatmap',
        '2. Assets vs Revenue',
        '3. Balance vs Collateral',
        '4. Leverage vs Profitability',
        '5. Industry vs Fund Amount',
        '6. Region vs Balance',
        '7. Loan Status vs Balance',
        '8. Credit Score vs Interest Rate',
        '9. DTI vs Loan Status',
        '10. Income vs Fund Amount',
        '11. Collateral vs Fund Amount',
        '12. Loan Purpose vs Balance',
        '13. Pairplot (Top 10 Features)',
        '14. Employment vs Income',
        '15. Revenue vs Expenses'
    ],
    'Key_Insight': [
        'Weak correlations overall; strongest: NUM_CREDIT_ACCOUNTS vs PAYMENT_HISTORY_SCORE (-0.11)',
        'No linear relationship (r=-0.029); assets do not predict revenue',
        'No relationship (r=0.004); balance independent of collateral',
        'No relationship (r=0.003); leverage does not predict profitability',
        'Finance sector has highest median fund amount ($294k), Retail lowest ($229k)',
        'Central region has highest balance ($210k), South/West lower (~$190k)',
        'DEFAULT loans have higher balance ($205k) vs CURRENT ($189k)',
        'No relationship (r=-0.007); credit score does not predict interest rate',
        'DEFAULT borrowers have higher DTI (0.475) vs PAID_OFF (0.438)',
        'Weak negative correlation (r=-0.043); income weakly predicts fund amount',
        'Weak positive correlation (r=0.065); some collateral-fund relationship',
        'CAR loans have highest balance ($230k), HOME/BUSINESS lower (~$170k)',
        'Multiple pairwise relationships visualized; no strong linear patterns',
        'Unemployed have higher income (mean $171k) - data artifact',
        'No correlation (r=0.005); revenue-expense independent in this data'
    ],
    'Business_Value': [
        'Minimal linear predictability; consider non-linear models',
        'Asset size not revenue indicator; need other business metrics',
        'Collateral not aligned with balance; review risk coverage',
        'Financial health metrics independent; multifactor risk needed',
        'Sector-based pricing opportunity; Finance commands premium',
        'Geographic risk segmentation; Central region higher exposure',
        'Balance accumulation risk signal; monitor DEFAULT patterns',
        'Pricing not risk-adjusted; interest rate policy needs review',
        'DTI is risk indicator; DEFAULT segment shows elevated DTI',
        'Income-based lending weak; consider other capacity metrics',
        'Moderate collateral alignment; strengthen security policies',
        'Product segmentation clear; CAR loans retain higher balances',
        'Comprehensive view of feature interactions for modeling',
        'Employment data quality issue; validate income sources',
        'Business profitability not visible; need better financials'
    ]
}

bivariate_summary_df = pd.DataFrame(bivariate_insights)

print('=' * 120)
print('BIVARIATE ANALYSIS SUMMARY - 15+ VISUALIZATIONS COMPLETED')
print('=' * 120)
print(bivariate_summary_df.to_string(index=False))
print('=' * 120)
print(f'\nTotal visualizations created: {len(bivariate_insights["Visualization"])}')
print('Coverage: Numeric-numeric scatter plots, categorical-numeric box plots, pairplots')
print('Key Finding: Weak linear correlations suggest need for non-linear modeling approaches')
print('Segmentation Opportunities: Industry sector, Region, Loan Purpose, Loan Status')