"""Configuration file for Hospital Management System."""

# Hospital Configuration
HOSPITAL_CONFIG = {
    "name": "City Medical Center",
    "location": "123 Healthcare Ave",
    "phone": "555-0100",
    "email": "info@citymedical.com",
    "total_beds": 500
}

# Department Configuration
DEPARTMENTS = [
    {"name": "Cardiology", "code": "CARD"},
    {"name": "Emergency", "code": "EMERG"},
    {"name": "Orthopedics", "code": "ORTHO"},
    {"name": "Neurology", "code": "NEURO"},
    {"name": "Pediatrics", "code": "PEDI"},
    {"name": "ICU", "code": "ICU"},
    {"name": "Psychiatry", "code": "PSY"},
]

# Staff Positions
STAFF_POSITIONS = [
    "Doctor",
    "Nurse",
    "Surgeon",
    "Administrator",
    "Receptionist",
    "Technician",
    "Specialist",
]

# Patient Statuses
PATIENT_STATUSES = [
    "Active",
    "In Recovery",
    "Discharged",
    "Critical",
    "Stable",
    "Observation",
]

# Data Directory
DATA_DIR = "data"
