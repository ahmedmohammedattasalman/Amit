"""Hospital service for managing hospital operations."""


class HospitalService:
    """Service class for hospital operations."""
    
    def __init__(self, hospital):
        """
        Initialize HospitalService.
        
        Args:
            hospital: Hospital instance
        """
        self.hospital = hospital
    
    def add_department(self, department):
        """Add a department to hospital."""
        return self.hospital.add_department(department)
    
    def remove_department(self, department_code):
        """Remove a department from hospital."""
        return self.hospital.remove_department(department_code)
    
    def get_hospital_info(self):
        """Get hospital information."""
        return self.hospital.view_info()
    
    def list_all_departments(self):
        """List all departments."""
        departments = self.hospital.list_departments()
        if isinstance(departments, list):
            return "\n".join(departments)
        return departments
    
    def get_department(self, code):
        """Get specific department."""
        return self.hospital.get_department(code)
    
    def get_available_beds(self):
        """Get available beds."""
        return self.hospital.get_bed_status()
    
    def occupy_bed(self):
        """Occupy a hospital bed."""
        if self.hospital.occupy_bed():
            return "Bed occupied successfully."
        return "No available beds."
    
    def free_bed(self):
        """Free a hospital bed."""
        if self.hospital.free_bed():
            return "Bed freed successfully."
        return "All beds are already free."
