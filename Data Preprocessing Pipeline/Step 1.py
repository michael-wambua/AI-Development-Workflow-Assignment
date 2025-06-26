# Data integration from multiple sources
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer

def integrate_data_sources():
    """
    Integrate data from EHR, administrative, and social determinant sources
    """
    # Load data from different sources
    ehr_data = pd.read_csv('ehr_records.csv')
    admin_data = pd.read_csv('administrative_data.csv')
    social_data = pd.read_csv('social_determinants.csv')
    
    # Merge on patient ID with proper handling of missing records
    merged_data = ehr_data.merge(admin_data, on='patient_id', how='left')
    merged_data = merged_data.merge(social_data, on='patient_id', how='left')
    
    return merged_data