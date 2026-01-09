"""Hospital Management System - Main Package"""

__version__ = "1.0.0"
__author__ = "Hospital System Developer"
__description__ = "A comprehensive hospital management system with pipeline architecture"

from models import Hospital, Patient, Staff, Department, Person
from services import HospitalService, PatientService, StaffService, DepartmentService
from ui import HospitalUI, MenuSystem

__all__ = [
    'Hospital',
    'Patient',
    'Staff',
    'Department',
    'Person',
    'HospitalService',
    'PatientService',
    'StaffService',
    'DepartmentService',
    'HospitalUI',
    'MenuSystem',
]
