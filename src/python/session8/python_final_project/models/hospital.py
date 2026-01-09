"""Hospital class for hospital system."""


class Hospital:
    """Class for managing hospital operations."""
    
    def __init__(self, name, location, phone, email):
        """
        Initialize a Hospital.
        
        Args:
            name (str): Hospital name
            location (str): Hospital address
            phone (str): Contact phone number
            email (str): Contact email
        """
        self.name = name
        self.location = location
        self.phone = phone
        self.email = email
        self.departments = {}  # Use dict for faster lookup
        self.total_beds = 0
        self.available_beds = 0
    
    def add_department(self, department):
        """Add a department to the hospital."""
        if department.code not in self.departments:
            self.departments[department.code] = department
            return f"Department '{department.name}' ({department.code}) added to {self.name}."
        return f"Department '{department.code}' already exists."
    
    def remove_department(self, department_code):
        """Remove a department from the hospital."""
        if department_code in self.departments:
            dept = self.departments.pop(department_code)
            return f"Department '{dept.name}' removed from {self.name}."
        return f"Department '{department_code}' not found."
    
    def get_department(self, department_code):
        """Get a specific department by code."""
        return self.departments.get(department_code, None)
    
    def list_departments(self):
        """List all departments in the hospital."""
        if not self.departments:
            return "No departments available."
        return [dept.view_info() for dept in self.departments.values()]
    
    def set_total_beds(self, total_beds):
        """Set total hospital beds."""
        self.total_beds = total_beds
        self.available_beds = total_beds
        return f"Total beds set to {total_beds}"
    
    def occupy_bed(self):
        """Occupy a bed."""
        if self.available_beds > 0:
            self.available_beds -= 1
            return True
        return False
    
    def free_bed(self):
        """Free a bed."""
        if self.available_beds < self.total_beds:
            self.available_beds += 1
            return True
        return False
    
    def get_bed_status(self):
        """Get bed availability status."""
        return f"Available beds: {self.available_beds}/{self.total_beds}"
    
    def view_info(self):
        """View hospital information."""
        dept_count = len(self.departments)
        return f"Hospital: {self.name}, Location: {self.location}, Departments: {dept_count}, {self.get_bed_status()}"
    
    def __repr__(self):
        """String representation of Hospital."""
        return f"Hospital(name='{self.name}', location='{self.location}')"
