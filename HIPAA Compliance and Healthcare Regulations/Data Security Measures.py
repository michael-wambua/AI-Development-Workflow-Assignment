import cryptography
from cryptography.fernet import Fernet
import hashlib

class HIPAACompliantDataHandler:
    """
    HIPAA-compliant data handling for patient information
    """
    
    def __init__(self):
        self.encryption_key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.encryption_key)
    
    def encrypt_phi(self, patient_data):
        """
        Encrypt Protected Health Information (PHI)
        """
        # Convert data to string and encrypt
        data_string = json.dumps(patient_data)
        encrypted_data = self.cipher_suite.encrypt(data_string.encode())
        return encrypted_data
    
    def decrypt_phi(self, encrypted_data):
        """
        Decrypt PHI for authorized access
        """
        decrypted_data = self.cipher_suite.decrypt(encrypted_data)
        return json.loads(decrypted_data.decode())
    
    def anonymize_data(self, patient_data):
        """
        De-identify patient data for research/analytics
        """
        # Remove direct identifiers
        anonymized = patient_data.copy()
        anonymized.pop('patient_id', None)
        anonymized.pop('name', None)
        anonymized.pop('ssn', None)
        anonymized.pop('address', None)
        
        # Generate pseudonym
        anonymized['patient_hash'] = hashlib.sha256(
            str(patient_data.get('patient_id', '')).encode()
        ).hexdigest()[:10]
        
        return anonymized