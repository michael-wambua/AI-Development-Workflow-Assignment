def clean_data(df):
    """
    Clean and validate data quality
    """
    # Remove duplicates
    df = df.drop_duplicates(subset=['patient_id', 'admission_date'])
    
    # Handle missing values strategically
    # For categorical variables, use mode imputation
    categorical_cols = ['gender', 'insurance_type', 'discharge_disposition']
    for col in categorical_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)
    
    # For numerical variables, use median imputation
    numerical_cols = ['age', 'length_of_stay', 'num_medications']
    imputer = SimpleImputer(strategy='median')
    df[numerical_cols] = imputer.fit_transform(df[numerical_cols])
    
    # Validate data ranges (e.g., age between 0-120)
    df = df[(df['age'] >= 0) & (df['age'] <= 120)]
    
    return df