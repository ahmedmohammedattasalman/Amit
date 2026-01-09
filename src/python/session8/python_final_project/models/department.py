"""Department class for hospital system."""


class Department:
    """Class representing a department in the hospital."""
    
    def __init__(self, name, code):
        """
        Initialize a Department.
        
        Args:
            name (str): Department name
            code (str): Department code (e.g., 'CARD', 'EMERG')
        """
        self.name = name
        self.code = code
        self.patients = []
        self.staff = []
        self.description = ""
    
    def add_patient(self, patient):
        """Add a patient to the department."""
        if patient not in self.patients:
            self.patients.append(patient)
            return f"Patient '{patient.name}' added to {self.name} department."
        return f"Patient '{patient.name}' already exists in {self.name} department."
    
    def remove_patient(self, patient):
        """Remove a patient from the department."""
        if patient in self.patients:
            self.patients.remove(patient)
            return f"Patient '{patient.name}' removed from {self.name} department."
        return f"Patient '{patient.name}' not found in {self.name} department."
    
    def add_staff(self, staff_member):
        """Add staff member to the department."""
        if staff_member not in self.staff:
            self.staff.append(staff_member)
            staff_member.department = self.name
            return f"Staff '{staff_member.name}' added to {self.name} department."
        return f"Staff '{staff_member.name}' already exists in {self.name} department."
    
    def remove_staff(self, staff_member):
        """Remove staff member from the department."""
        if staff_member in self.staff:
            self.staff.remove(staff_member)
            return f"Staff '{staff_member.name}' removed from {self.name} department."
        return f"Staff '{staff_member.name}' not found in {self.name} department."
    
    def get_patients_count(self):
        """Get number of patients in department."""
        return len(self.patients)
    
    def get_staff_count(self):
        """Get number of staff members in department."""
        return len(self.staff)
    
    def view_info(self):
        """View department information."""
        return f"Department: {self.name} ({self.code}), Patients: {self.get_patients_count()}, Staff: {self.get_staff_count()}"
    
    def __repr__(self):
        """String representation of Department."""
        return f"Department(name='{self.name}', code='{self.code}')"
