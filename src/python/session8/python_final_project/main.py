"""Main entry point for Hospital Management System."""
import sys
import os

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models import Hospital, Department, Patient, Staff
from ui import HospitalUI


def initialize_hospital():
    """Initialize hospital with sample data."""
    # Create hospital
    hospital = Hospital("City Medical Center", "123 Healthcare Ave", "555-0100", "info@citymedical.com")
    hospital.set_total_beds(500)
    
    # Create departments
    departments = [
        Department("Cardiology", "CARD"),
        Department("Emergency", "EMERG"),
        Department("Orthopedics", "ORTHO"),
        Department("Neurology", "NEURO"),
        Department("Pediatrics", "PEDI"),
    ]
    
    for dept in departments:
        hospital.add_department(dept)
    
    return hospital


def main():
    """Main function to run the hospital management system."""
    print("\n" + "="*50)
    print("   Welcome to Hospital Management System")
    print("="*50)
    
    # Initialize hospital
    hospital = initialize_hospital()
    print("\n✓ Hospital initialized successfully!")
    print(f"✓ Hospital: {hospital.name}")
    print(f"✓ Location: {hospital.location}")
    print(f"✓ Total Beds: {hospital.total_beds}")
    print(f"✓ Departments: {len(hospital.departments)}")
    
    # Start UI
    ui = HospitalUI(hospital)
    ui.run()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nError: {e}")
        print("The application encountered an unexpected error.")
