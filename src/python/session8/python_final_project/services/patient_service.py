"""Patient service for managing patient operations."""


class PatientService:
    """Service class for patient operations."""
    
    def __init__(self):
        """Initialize PatientService."""
        self.patients = {}
    
    def register_patient(self, patient):
        """Register a new patient."""
        if patient.id_number not in self.patients:
            self.patients[patient.id_number] = patient
            return f"Patient {patient.name} registered successfully."
        return f"Patient with ID {patient.id_number} already exists."
    
    def get_patient(self, patient_id):
        """Get patient by ID."""
        return self.patients.get(patient_id, None)
    
    def update_patient_record(self, patient_id, new_record):
        """Update patient medical record."""
        if patient_id in self.patients:
            patient = self.patients[patient_id]
            return patient.update_record(new_record)
        return f"Patient with ID {patient_id} not found."
    
    def update_patient_status(self, patient_id, status):
        """Update patient status."""
        if patient_id in self.patients:
            patient = self.patients[patient_id]
            return patient.update_status(status)
        return f"Patient with ID {patient_id} not found."
    
    def remove_patient(self, patient_id):
        """Remove patient from system."""
        if patient_id in self.patients:
            patient = self.patients.pop(patient_id)
            return f"Patient {patient.name} removed from system."
        return f"Patient with ID {patient_id} not found."
    
    def list_all_patients(self):
        """List all patients."""
        if not self.patients:
            return "No patients registered."
        return [patient.view_record() for patient in self.patients.values()]
    
    def get_patients_by_status(self, status):
        """Get patients by status."""
        result = [p for p in self.patients.values() if p.status == status]
        return result if result else f"No patients with status '{status}'."
    
    def get_total_patients(self):
        """Get total number of patients."""
        return len(self.patients)
