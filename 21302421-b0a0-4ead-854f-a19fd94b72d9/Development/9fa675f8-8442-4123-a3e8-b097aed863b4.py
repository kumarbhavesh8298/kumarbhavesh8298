import pandas as pd

# Define expected schema with data types
expected_schema = {
    'CUST_ID': 'int64',
    'CUST_OPN_DT': 'datetime64[ns]',
    'BRTH_DT': 'datetime64[ns]',
    'FIRST_DISBT_DT': 'datetime64[ns]',
    'OCCP_CODE': 'object',
    'INDUSTRY_SECTOR': 'object',
    'MARITAL_STATUS': 'object',
    'FUND_AMT': 'float64',
    'BALANCE': 'float64',
    'TOTAL_ASSETS': 'float64',
    'TOTAL_LIABILITIES': 'float64',
    'ANNUAL_INCOME': 'float64',
    'CREDIT_SCORE': 'int64',
    'LOAN_TERM': 'int64',
    'INTEREST_RATE': 'float64',
    'PAYMENT_FREQUENCY': 'object',
    'COLLATERAL_VALUE': 'float64',
    'LOAN_PURPOSE': 'object',
    'EMPLOYMENT_STATUS': 'object',
    'YEARS_EMPLOYED': 'int64',
    'DEBT_TO_INCOME': 'float64',
    'NUM_DEPENDENTS': 'int64',
    'EDUCATION_LEVEL': 'object',
    'HOME_OWNERSHIP': 'object',
    'REGION': 'object',
    'CITY_TIER': 'int64',
    'PREVIOUS_DEFAULTS': 'int64',
    'CREDIT_HISTORY_LENGTH': 'int64',
    'NUM_CREDIT_ACCOUNTS': 'int64',
    'CREDIT_UTILIZATION': 'float64',
    'NUM_RECENT_INQUIRIES': 'int64',
    'PAYMENT_HISTORY_SCORE': 'float64',
    'LOAN_STATUS': 'object',
    'DAYS_PAST_DUE': 'int64',
    'NUM_PAYMENTS_MADE': 'int64',
    'TOTAL_PAID': 'float64',
    'REMAINING_BALANCE': 'float64',
    'LAST_PAYMENT_DATE': 'datetime64[ns]',
    'NEXT_PAYMENT_DATE': 'datetime64[ns]',
    'BUSINESS_REVENUE': 'float64',
    'BUSINESS_EXPENSES': 'float64',
    'NET_PROFIT': 'float64',
    'CASH_FLOW': 'float64',
    'OPERATING_PROFIT': 'float64'
}

# Validate schema
schema_errors = []

# Check for missing columns
missing_cols = set(expected_schema.keys()) - set(loan_df.columns)
if missing_cols:
    schema_errors.append(f"Missing columns: {missing_cols}")

# Check for extra columns
extra_cols = set(loan_df.columns) - set(expected_schema.keys())
if extra_cols:
    schema_errors.append(f"Unexpected columns: {extra_cols}")

# Check data types
dtype_mismatches = []
for col, expected_dtype in expected_schema.items():
    if col in loan_df.columns:
        actual_dtype = str(loan_df[col].dtype)
        if actual_dtype != expected_dtype:
            dtype_mismatches.append(f"{col}: expected {expected_dtype}, got {actual_dtype}")

if dtype_mismatches:
    schema_errors.append(f"Data type mismatches: {dtype_mismatches}")

# Output validation results
if schema_errors:
    validation_result = "SCHEMA VALIDATION FAILED"
    print(validation_result)
    for error in schema_errors:
        print(f"  - {error}")
else:
    validation_result = "SCHEMA VALIDATION PASSED"
    print(validation_result)
    print("✓ All 44 columns present")
    print("✓ All data types correct")
    print("✓ Date columns properly formatted")