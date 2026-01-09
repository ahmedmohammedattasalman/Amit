"""Models package for hospital system."""
from .person import Person
from .patient import Patient
from .staff import Staff
from .department import Department
from .hospital import Hospital

__all__ = ['Person', 'Patient', 'Staff', 'Department', 'Hospital']
