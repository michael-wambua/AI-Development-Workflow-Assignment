def encode_and_normalize(df):
    """
    Encode categorical variables and normalize numerical features
    """
    # Label encode categorical variables
    label_encoders = {}
    categorical_cols = ['gender', 'insurance_type', 'discharge_disposition', 'age_group']
    
    for col in categorical_cols:
        le = LabelEncoder()
        df[col + '_encoded'] = le.fit_transform(df[col])
        label_encoders[col] = le
    
    # Standardize numerical features
    numerical_cols = ['age', 'length_of_stay', 'charlson_score', 'medication_complexity']
    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
    
    return df, label_encoders, scaler