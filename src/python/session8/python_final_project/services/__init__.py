"""Services package for hospital system."""
from .hospital_service import HospitalService
from .patient_service import PatientService
from .staff_service import StaffService
from .department_service import DepartmentService

__all__ = ['HospitalService', 'PatientService', 'StaffService', 'DepartmentService']
