"""Staff class for hospital system."""
from .person import Person


class Staff(Person):
    """Class for hospital staff, inheriting from Person."""
    
    def __init__(self, name, age, id_number, position, department=None, salary=None):
        """
        Initialize a Staff member.
        
        Args:
            name (str): Staff member's name
            age (int): Staff member's age
            id_number (str): Unique staff ID
            position (str): Job position (Doctor, Nurse, Administrator, etc.)
            department (str): Department assignment
            salary (float): Monthly salary
        """
        super().__init__(name, age, id_number)
        self.position = position
        self.department = department
        self.salary = salary
        self.schedule = []
    
    def view_info(self):
        """View staff information."""
        return f"Staff: {self.name}, ID: {self.id_number}, Position: {self.position}, Department: {self.department}"
    
    def set_schedule(self, schedule):
        """Set work schedule."""
        self.schedule = schedule
        return f"Schedule set for {self.name}: {schedule}"
    
    def get_schedule(self):
        """Get work schedule."""
        return self.schedule if self.schedule else "No schedule set"
    
    def __repr__(self):
        """String representation of Staff."""
        return f"Staff(name='{self.name}', position='{self.position}', department='{self.department}')"
