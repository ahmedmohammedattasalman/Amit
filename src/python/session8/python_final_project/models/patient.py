"""Patient class for hospital system."""
from .person import Person


class Patient(Person):
    """Class for hospital patients, inheriting from Person."""
    
    def __init__(self, name, age, id_number, medical_record, admission_date=None):
        """
        Initialize a Patient.
        
        Args:
            name (str): Patient's name
            age (int): Patient's age
            id_number (str): Unique patient ID
            medical_record (str): Medical history/record
            admission_date (str): Date of admission
        """
        super().__init__(name, age, id_number)
        self.medical_record = medical_record
        self.admission_date = admission_date
        self.status = "Active"  # Active, Discharged, In Recovery, etc.
    
    def view_record(self):
        """View patient record."""
        return f"Patient: {self.name}, ID: {self.id_number}, Record: {self.medical_record}, Status: {self.status}"
    
    def update_record(self, new_record):
        """Update patient medical record."""
        self.medical_record = new_record
        return f"Record updated for {self.name}"
    
    def update_status(self, status):
        """Update patient status."""
        self.status = status
        return f"Status updated to {status} for {self.name}"
    
    def __repr__(self):
        """String representation of Patient."""
        return f"Patient(name='{self.name}', id='{self.id_number}', status='{self.status}')"
