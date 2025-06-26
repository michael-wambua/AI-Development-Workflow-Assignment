class AccessControlSystem:
    """
    Role-based access control for AI prediction system
    """
    
    def __init__(self):
        self.user_roles = {
            'physician': ['view_predictions', 'view_patient_data'],
            'nurse': ['view_predictions'],
            'admin': ['view_predictions', 'view_analytics', 'manage_system'],
            'researcher': ['view_anonymized_data']
        }
    
    def check_permission(self, user_id, action):
        """
        Check if user has permission for requested action
        """
        user_role = self.get_user_role(user_id)
        return action in self.user_roles.get(user_role, [])
    
    def log_access(self, user_id, action, patient_id=None):
        """
        Log all access attempts for HIPAA audit trail
        """
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'user_id': user_id,
            'action': action,
            'patient_id': patient_id,
            'ip_address': request.remote_addr,
            'success': True
        }
        
        # Store in secure audit log
        self.store_audit_log(log_entry)