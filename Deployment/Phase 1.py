# API endpoint for model predictions
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model and preprocessing components
model = joblib.load('readmission_model.pkl')
scaler = joblib.load('feature_scaler.pkl')
encoders = joblib.load('label_encoders.pkl')

@app.route('/predict_readmission', methods=['POST'])
def predict_readmission():
    """
    API endpoint for readmission risk prediction
    """
    try:
        # Get patient data from request
        patient_data = request.get_json()
        
        # Validate required fields
        required_fields = ['age', 'length_of_stay', 'charlson_score', 
                          'gender', 'insurance_type']
        for field in required_fields:
            if field not in patient_data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Preprocess data
        processed_data = preprocess_patient_data(patient_data)
        
        # Make prediction
        risk_probability = model.predict_proba([processed_data])[0][1]
        risk_category = 'High' if risk_probability > 0.5 else 'Low'
        
        # Log prediction for audit trail
        log_prediction(patient_data['patient_id'], risk_probability)
        
        return jsonify({
            'patient_id': patient_data['patient_id'],
            'readmission_risk_probability': float(risk_probability),
            'risk_category': risk_category,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def preprocess_patient_data(patient_data):
    """
    Apply same preprocessing as training data
    """
    # Convert to DataFrame for consistent processing
    df = pd.DataFrame([patient_data])
    
    # Apply feature engineering
    df = engineer_features(df)
    
    # Apply encoding and scaling
    df, _, _ = encode_and_normalize(df)
    
    # Return feature vector
    return df.iloc[0].values