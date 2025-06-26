def engineer_features(df):
    """
    Create relevant features for readmission prediction
    """
    # Calculate Charlson Comorbidity Index
    df['charlson_score'] = calculate_charlson_index(df)
    
    # Create age groups
    df['age_group'] = pd.cut(df['age'], bins=[0, 30, 50, 70, 100], 
                            labels=['Young', 'Middle', 'Senior', 'Elderly'])
    
    # Previous admission frequency (last 12 months)
    df['prev_admissions_12mo'] = calculate_previous_admissions(df)
    
    # Length of stay categories
    df['los_category'] = pd.cut(df['length_of_stay'], 
                               bins=[0, 3, 7, 14, float('inf')],
                               labels=['Short', 'Medium', 'Long', 'Extended'])
    
    # Medication complexity score
    df['medication_complexity'] = calculate_medication_complexity(df)
    
    # Social risk score
    df['social_risk_score'] = calculate_social_risk(df)
    
    return df

def calculate_charlson_index(df):
    """Calculate Charlson Comorbidity Index based on diagnosis codes"""
    # Simplified example - would use actual ICD codes in practice
    charlson_weights = {
        'diabetes': 1,
        'heart_failure': 2,
        'copd': 1,
        'cancer': 2,
        'kidney_disease': 2
    }
    
    score = 0
    for condition, weight in charlson_weights.items():
        if condition in df.columns:
            score += df[condition] * weight
    
    return score