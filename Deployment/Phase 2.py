class EHRIntegration:
    """
    Integration layer with hospital EHR system
    """
    
    def __init__(self, ehr_endpoint, api_key):
        self.ehr_endpoint = ehr_endpoint
        self.api_key = api_key
    
    def get_patient_data(self, patient_id):
        """
        Retrieve patient data from EHR system
        """
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.get(
            f'{self.ehr_endpoint}/patients/{patient_id}',
            headers=headers
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Failed to retrieve patient data: {response.status_code}')
    
    def update_risk_score(self, patient_id, risk_score):
        """
        Update patient record with readmission risk score
        """
        headers = {'Authorization': f'Bearer {self.api_key}'}
        data = {
            'readmission_risk_score': risk_score,
            'last_updated': datetime.now().isoformat()
        }
        
        response = requests.put(
            f'{self.ehr_endpoint}/patients/{patient_id}/risk_scores',
            headers=headers,
            json=data
        )
        
        return response.status_code == 200