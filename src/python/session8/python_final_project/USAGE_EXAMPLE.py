"""
Complete Usage Example - Hospital Management System
=====================================================

This file demonstrates how to use the Hospital Management System
programmatically without the interactive UI.
"""

# Example 1: Basic Hospital Setup
print("="*60)
print("Example 1: Hospital Setup")
print("="*60)

from models import Hospital, Department, Patient, Staff
from services import HospitalService, PatientService, StaffService, DepartmentService

# Create hospital
hospital = Hospital("St. Mary's Medical Center", "456 Medical Plaza", "555-1234", "contact@stmarys.com")
hospital.set_total_beds(300)

service = HospitalService(hospital)
print(service.get_hospital_info())

# Add departments
cardiology = Department("Cardiology", "CARD")
emergency = Department("Emergency", "EMERG")
orthopedics = Department("Orthopedics", "ORTHO")

hospital.add_department(cardiology)
hospital.add_department(emergency)
hospital.add_department(orthopedics)

print(f"\nDepartments added: {service.list_all_departments()}")


# Example 2: Patient Management
print("\n" + "="*60)
print("Example 2: Patient Management")
print("="*60)

patient_service = PatientService()

# Create and register patients
patients = [
    Patient("John Smith", 55, "PAT001", "Heart condition, on medication"),
    Patient("Sarah Johnson", 42, "PAT002", "Hypertension"),
    Patient("Michael Brown", 68, "PAT003", "Diabetes, arthritis"),
]

for patient in patients:
    print(patient_service.register_patient(patient))

# Add patients to departments
cardiology.add_patient(patients[0])
cardiology.add_patient(patients[1])
orthopedics.add_patient(patients[2])

print(f"\nPatients in Cardiology: {cardiology.get_patients_count()}")
print(f"Patients in Orthopedics: {orthopedics.get_patients_count()}")

# Update patient status
print("\n" + patient_service.update_patient_status("PAT001", "In Recovery"))
print(patient_service.update_patient_record("PAT001", "Completed initial tests. Stable condition."))

# List all patients
print("\nAll Patients:")
for patient_info in patient_service.list_all_patients():
    print(f"  - {patient_info}")


# Example 3: Staff Management
print("\n" + "="*60)
print("Example 3: Staff Management")
print("="*60)

staff_service = StaffService()

# Create and hire staff
staff_members = [
    Staff("Dr. Alice Williams", 55, "STAFF001", "Cardiologist", "Cardiology", 150000),
    Staff("Dr. Robert Taylor", 48, "STAFF002", "Surgeon", "Orthopedics", 140000),
    Staff("Nurse Emily Davis", 35, "STAFF003", "Registered Nurse", "Emergency", 65000),
    Staff("Nurse James Martinez", 40, "STAFF004", "Registered Nurse", "Cardiology", 70000),
]

for staff in staff_members:
    print(staff_service.hire_staff(staff))
    cardiology.add_staff(staff) if staff.position == "Cardiologist" else None
    orthopedics.add_staff(staff) if staff.position == "Surgeon" else None

# Set schedules
print("\n" + staff_service.set_schedule("STAFF001", "Mon-Fri 8AM-4PM, Weekend On-Call"))
print(staff_service.set_schedule("STAFF003", "Rotating 12-hour shifts"))

# List staff
print("\nAll Staff:")
for staff_info in staff_service.list_all_staff():
    print(f"  - {staff_info}")


# Example 4: Department Management
print("\n" + "="*60)
print("Example 4: Department Management")
print("="*60)

dept_service = DepartmentService()

# Create departments using service
dept_service.create_department(cardiology)
dept_service.create_department(emergency)
dept_service.create_department(orthopedics)

# View department info
print("\nCardiology Department Info:")
print(cardiology.view_info())

print("\nEmergency Department Info:")
print(emergency.view_info())

print("\nOrthopedics Department Info:")
print(orthopedics.view_info())


# Example 5: Hospital Resources
print("\n" + "="*60)
print("Example 5: Hospital Resources Management")
print("="*60)

print(f"Initial bed status: {service.get_available_beds()}")

# Occupy some beds
for i in range(5):
    result = service.occupy_bed()
    print(f"Action: {result}")

print(f"Updated bed status: {service.get_available_beds()}")

# Free some beds
for i in range(2):
    result = service.free_bed()
    print(f"Action: {result}")

print(f"Final bed status: {service.get_available_beds()}")


# Example 6: Query Examples
print("\n" + "="*60)
print("Example 6: Query and Reporting")
print("="*60)

# Get specific patient
print("\nQuerying Patient PAT001:")
patient = patient_service.get_patient("PAT001")
if patient:
    print(f"  Name: {patient.name}")
    print(f"  Age: {patient.age}")
    print(f"  Status: {patient.status}")
    print(f"  Record: {patient.medical_record}")

# Get patients by status
print("\nPatients in 'In Recovery' status:")
recovery_patients = patient_service.get_patients_by_status("In Recovery")
if isinstance(recovery_patients, list):
    for p in recovery_patients:
        print(f"  - {p.name}")

# Get staff by department
print("\nStaff in Cardiology Department:")
cardio_staff = staff_service.get_staff_by_department("Cardiology")
if isinstance(cardio_staff, list):
    for s in cardio_staff:
        print(f"  - {s.name} ({s.position})")

# Summary Statistics
print("\n" + "="*60)
print("System Summary Statistics")
print("="*60)
print(f"Total Patients: {patient_service.get_total_patients()}")
print(f"Total Staff: {staff_service.get_total_staff()}")
print(f"Total Departments: {dept_service.get_total_departments()}")
print(f"Hospital Total Beds: {hospital.total_beds}")
print(f"Available Beds: {hospital.available_beds}")
print(f"Occupied Beds: {hospital.total_beds - hospital.available_beds}")


# Example 7: Data Validation
print("\n" + "="*60)
print("Example 7: Error Handling")
print("="*60)

# Try to register duplicate patient
print("\nAttempting to register duplicate patient:")
duplicate = Patient("John Smith", 55, "PAT001", "Duplicate entry")
print(patient_service.register_patient(duplicate))

# Try to get non-existent patient
print("\nAttempting to get non-existent patient:")
non_existent = patient_service.get_patient("PAT999")
if non_existent:
    print(f"Patient found: {non_existent.name}")
else:
    print("Patient not found (PAT999)")

# Try to update non-existent staff
print("\nAttempting to update non-existent staff:")
result = staff_service.update_position("STAFF999", "Consultant")
print(result)


print("\n" + "="*60)
print("Example Run Complete!")
print("="*60)
print("\nThis demonstrates the complete pipeline architecture:")
print("✓ Model creation (Hospital, Department, Patient, Staff)")
print("✓ Service operations (register, update, query)")
print("✓ Resource management (beds, assignments)")
print("✓ Error handling (duplicate, non-existent records)")
print("✓ Data integrity (unique IDs, validation)")
print("\nRun main.py for interactive UI version!")
