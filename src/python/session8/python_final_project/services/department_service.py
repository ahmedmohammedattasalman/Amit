"""Department service for managing department operations."""


class DepartmentService:
    """Service class for department operations."""
    
    def __init__(self):
        """Initialize DepartmentService."""
        self.departments = {}
    
    def create_department(self, department):
        """Create a new department."""
        if department.code not in self.departments:
            self.departments[department.code] = department
            return f"Department '{department.name}' created successfully."
        return f"Department '{department.code}' already exists."
    
    def get_department(self, department_code):
        """Get department by code."""
        return self.departments.get(department_code, None)
    
    def add_patient_to_department(self, department_code, patient):
        """Add patient to department."""
        if department_code in self.departments:
            dept = self.departments[department_code]
            return dept.add_patient(patient)
        return f"Department '{department_code}' not found."
    
    def remove_patient_from_department(self, department_code, patient):
        """Remove patient from department."""
        if department_code in self.departments:
            dept = self.departments[department_code]
            return dept.remove_patient(patient)
        return f"Department '{department_code}' not found."
    
    def add_staff_to_department(self, department_code, staff_member):
        """Add staff to department."""
        if department_code in self.departments:
            dept = self.departments[department_code]
            return dept.add_staff(staff_member)
        return f"Department '{department_code}' not found."
    
    def remove_staff_from_department(self, department_code, staff_member):
        """Remove staff from department."""
        if department_code in self.departments:
            dept = self.departments[department_code]
            return dept.remove_staff(staff_member)
        return f"Department '{department_code}' not found."
    
    def list_all_departments(self):
        """List all departments."""
        if not self.departments:
            return "No departments available."
        return [dept.view_info() for dept in self.departments.values()]
    
    def get_department_info(self, department_code):
        """Get department information."""
        if department_code in self.departments:
            return self.departments[department_code].view_info()
        return f"Department '{department_code}' not found."
    
    def get_total_departments(self):
        """Get total number of departments."""
        return len(self.departments)
