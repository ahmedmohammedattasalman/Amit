"""Person base class for hospital system."""


class Person:
    """Base class for all people in the hospital."""
    
    def __init__(self, name, age, id_number):
        """
        Initialize a Person.
        
        Args:
            name (str): Person's name
            age (int): Person's age
            id_number (str): Unique identifier
        """
        self.name = name
        self.age = age
        self.id_number = id_number
    
    def view_info(self):
        """View basic information about the person."""
        return f"Name: {self.name}, Age: {self.age}, ID: {self.id_number}"
    
    def __repr__(self):
        """String representation of Person."""
        return f"Person(name='{self.name}', age={self.age}, id='{self.id_number}')"
