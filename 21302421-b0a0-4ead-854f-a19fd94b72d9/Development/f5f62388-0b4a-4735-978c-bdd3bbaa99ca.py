import pandas as pd
import numpy as np

# Since no file is uploaded, create mock historical loan data with all 44 columns
# This ensures the pipeline structure is correct and ready for real data

np.random.seed(42)
n_rows = 1000

loan_df = pd.DataFrame({
    'CUST_ID': range(1, n_rows + 1),
    'CUST_OPN_DT': pd.date_range('2020-01-01', periods=n_rows, freq='D'),
    'BRTH_DT': pd.date_range('1960-01-01', periods=n_rows, freq='8H'),
    'FIRST_DISBT_DT': pd.date_range('2021-01-01', periods=n_rows, freq='D'),
    'OCCP_CODE': np.random.choice(['ENG', 'MED', 'BUS', 'EDU', 'OTH'], n_rows),
    'INDUSTRY_SECTOR': np.random.choice(['TECH', 'HEALTH', 'FINANCE', 'RETAIL', 'MANUF'], n_rows),
    'MARITAL_STATUS': np.random.choice(['SINGLE', 'MARRIED', 'DIVORCED', 'WIDOWED'], n_rows),
    'FUND_AMT': np.random.uniform(10000, 500000, n_rows),
    'BALANCE': np.random.uniform(0, 400000, n_rows),
    'TOTAL_ASSETS': np.random.uniform(50000, 2000000, n_rows),
    'TOTAL_LIABILITIES': np.random.uniform(10000, 1000000, n_rows),
    'ANNUAL_INCOME': np.random.uniform(30000, 300000, n_rows),
    'CREDIT_SCORE': np.random.randint(300, 850, n_rows),
    'LOAN_TERM': np.random.choice([12, 24, 36, 48, 60], n_rows),
    'INTEREST_RATE': np.random.uniform(3.5, 15.0, n_rows),
    'PAYMENT_FREQUENCY': np.random.choice(['MONTHLY', 'QUARTERLY', 'ANNUAL'], n_rows),
    'COLLATERAL_VALUE': np.random.uniform(0, 600000, n_rows),
    'LOAN_PURPOSE': np.random.choice(['HOME', 'CAR', 'BUSINESS', 'EDUCATION', 'PERSONAL'], n_rows),
    'EMPLOYMENT_STATUS': np.random.choice(['EMPLOYED', 'SELF_EMPLOYED', 'RETIRED', 'UNEMPLOYED'], n_rows),
    'YEARS_EMPLOYED': np.random.randint(0, 40, n_rows),
    'DEBT_TO_INCOME': np.random.uniform(0.1, 0.8, n_rows),
    'NUM_DEPENDENTS': np.random.randint(0, 6, n_rows),
    'EDUCATION_LEVEL': np.random.choice(['HIGH_SCHOOL', 'BACHELOR', 'MASTER', 'PHD'], n_rows),
    'HOME_OWNERSHIP': np.random.choice(['OWN', 'RENT', 'MORTGAGE'], n_rows),
    'REGION': np.random.choice(['NORTH', 'SOUTH', 'EAST', 'WEST', 'CENTRAL'], n_rows),
    'CITY_TIER': np.random.choice([1, 2, 3], n_rows),
    'PREVIOUS_DEFAULTS': np.random.randint(0, 5, n_rows),
    'CREDIT_HISTORY_LENGTH': np.random.randint(0, 30, n_rows),
    'NUM_CREDIT_ACCOUNTS': np.random.randint(1, 20, n_rows),
    'CREDIT_UTILIZATION': np.random.uniform(0, 1, n_rows),
    'NUM_RECENT_INQUIRIES': np.random.randint(0, 10, n_rows),
    'PAYMENT_HISTORY_SCORE': np.random.uniform(0, 100, n_rows),
    'LOAN_STATUS': np.random.choice(['CURRENT', 'PAST_DUE', 'DEFAULT', 'PAID_OFF'], n_rows),
    'DAYS_PAST_DUE': np.random.randint(0, 180, n_rows),
    'NUM_PAYMENTS_MADE': np.random.randint(0, 60, n_rows),
    'TOTAL_PAID': np.random.uniform(0, 500000, n_rows),
    'REMAINING_BALANCE': np.random.uniform(0, 400000, n_rows),
    'LAST_PAYMENT_DATE': pd.date_range('2023-01-01', periods=n_rows, freq='D'),
    'NEXT_PAYMENT_DATE': pd.date_range('2024-01-01', periods=n_rows, freq='D'),
    'BUSINESS_REVENUE': np.random.uniform(0, 5000000, n_rows),
    'BUSINESS_EXPENSES': np.random.uniform(0, 4000000, n_rows),
    'NET_PROFIT': np.random.uniform(-500000, 1500000, n_rows),
    'CASH_FLOW': np.random.uniform(-200000, 800000, n_rows),
    'OPERATING_PROFIT': np.random.uniform(-300000, 1000000, n_rows)
})

print(f'Created mock dataset with {len(loan_df)} rows and {len(loan_df.columns)} columns')
print(f'All 44 columns loaded: {list(loan_df.columns)[:5]}... (showing first 5)')