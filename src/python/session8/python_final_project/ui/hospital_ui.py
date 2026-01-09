"""Hospital UI for user interaction."""
from .menu_system import MenuSystem
from models import Patient, Staff, Department
from services import HospitalService, PatientService, StaffService, DepartmentService


class HospitalUI:
    """User interface for hospital management system."""
    
    def __init__(self, hospital):
        """
        Initialize HospitalUI.
        
        Args:
            hospital: Hospital instance
        """
        self.hospital = hospital
        self.hospital_service = HospitalService(hospital)
        self.patient_service = PatientService()
        self.staff_service = StaffService()
        self.department_service = DepartmentService()
        self.menu = MenuSystem()
    
    def run(self):
        """Run the main application loop."""
        while True:
            self.menu.display_main_menu()
            choice = self.menu.get_input()
            
            if choice == '1':
                self.hospital_operations()
            elif choice == '2':
                self.patient_management()
            elif choice == '3':
                self.staff_management()
            elif choice == '4':
                self.department_management()
            elif choice == '5':
                self.view_system_status()
            elif choice == '0':
                print("\nThank you for using Hospital Management System. Goodbye!")
                break
            else:
                self.menu.print_error("Invalid choice. Please try again.")
    
    def hospital_operations(self):
        """Handle hospital operations."""
        while True:
            self.menu.display_hospital_menu()
            choice = self.menu.get_input()
            
            if choice == '1':
                info = self.hospital_service.get_hospital_info()
                self.menu.print_info(info)
            elif choice == '2':
                depts = self.hospital_service.list_all_departments()
                print("\nDepartments:")
                print(depts)
            elif choice == '3':
                beds = self.hospital_service.get_available_beds()
                self.menu.print_info(beds)
            elif choice == '4':
                result = self.hospital_service.occupy_bed()
                if "successfully" in result:
                    self.menu.print_success(result)
                else:
                    self.menu.print_error(result)
            elif choice == '5':
                result = self.hospital_service.free_bed()
                if "successfully" in result:
                    self.menu.print_success(result)
                else:
                    self.menu.print_error(result)
            elif choice == '0':
                break
            else:
                self.menu.print_error("Invalid choice. Please try again.")
    
    def patient_management(self):
        """Handle patient management."""
        while True:
            self.menu.display_patient_menu()
            choice = self.menu.get_input()
            
            if choice == '1':
                self.register_patient()
            elif choice == '2':
                self.view_patient()
            elif choice == '3':
                self.update_patient_record()
            elif choice == '4':
                self.update_patient_status()
            elif choice == '5':
                patients = self.patient_service.list_all_patients()
                if isinstance(patients, list):
                    print("\nPatients:")
                    for p in patients:
                        print(f"  - {p}")
                else:
                    self.menu.print_info(patients)
            elif choice == '6':
                patient_id = self.menu.get_input("Enter patient ID to remove: ")
                result = self.patient_service.remove_patient(patient_id)
                if "removed" in result:
                    self.menu.print_success(result)
                else:
                    self.menu.print_error(result)
            elif choice == '0':
                break
            else:
                self.menu.print_error("Invalid choice. Please try again.")
    
    def register_patient(self):
        """Register a new patient."""
        try:
            name = self.menu.get_input("Enter patient name: ")
            age = int(self.menu.get_input("Enter patient age: "))
            patient_id = self.menu.get_input("Enter patient ID: ")
            medical_record = self.menu.get_input("Enter medical record: ")
            
            patient = Patient(name, age, patient_id, medical_record)
            result = self.patient_service.register_patient(patient)
            self.menu.print_success(result)
        except ValueError:
            self.menu.print_error("Invalid input. Age must be a number.")
    
    def view_patient(self):
        """View patient information."""
        patient_id = self.menu.get_input("Enter patient ID: ")
        patient = self.patient_service.get_patient(patient_id)
        if patient:
            print(f"\n{patient.view_record()}")
        else:
            self.menu.print_error(f"Patient with ID {patient_id} not found.")
    
    def update_patient_record(self):
        """Update patient medical record."""
        patient_id = self.menu.get_input("Enter patient ID: ")
        new_record = self.menu.get_input("Enter new medical record: ")
        result = self.patient_service.update_patient_record(patient_id, new_record)
        if "updated" in result:
            self.menu.print_success(result)
        else:
            self.menu.print_error(result)
    
    def update_patient_status(self):
        """Update patient status."""
        patient_id = self.menu.get_input("Enter patient ID: ")
        print("Available statuses: Active, Discharged, In Recovery, Critical")
        status = self.menu.get_input("Enter new status: ")
        result = self.patient_service.update_patient_status(patient_id, status)
        if "updated" in result:
            self.menu.print_success(result)
        else:
            self.menu.print_error(result)
    
    def staff_management(self):
        """Handle staff management."""
        while True:
            self.menu.display_staff_menu()
            choice = self.menu.get_input()
            
            if choice == '1':
                self.hire_staff()
            elif choice == '2':
                self.view_staff()
            elif choice == '3':
                self.update_staff_position()
            elif choice == '4':
                self.set_staff_schedule()
            elif choice == '5':
                staff = self.staff_service.list_all_staff()
                if isinstance(staff, list):
                    print("\nStaff Members:")
                    for s in staff:
                        print(f"  - {s}")
                else:
                    self.menu.print_info(staff)
            elif choice == '6':
                staff_id = self.menu.get_input("Enter staff ID to remove: ")
                result = self.staff_service.remove_staff(staff_id)
                if "removed" in result:
                    self.menu.print_success(result)
                else:
                    self.menu.print_error(result)
            elif choice == '0':
                break
            else:
                self.menu.print_error("Invalid choice. Please try again.")
    
    def hire_staff(self):
        """Hire a new staff member."""
        try:
            name = self.menu.get_input("Enter staff name: ")
            age = int(self.menu.get_input("Enter staff age: "))
            staff_id = self.menu.get_input("Enter staff ID: ")
            position = self.menu.get_input("Enter position (Doctor, Nurse, Administrator, etc.): ")
            salary = float(self.menu.get_input("Enter salary: "))
            
            staff = Staff(name, age, staff_id, position, salary=salary)
            result = self.staff_service.hire_staff(staff)
            self.menu.print_success(result)
        except ValueError:
            self.menu.print_error("Invalid input. Age and salary must be numbers.")
    
    def view_staff(self):
        """View staff information."""
        staff_id = self.menu.get_input("Enter staff ID: ")
        staff = self.staff_service.get_staff_member(staff_id)
        if staff:
            print(f"\n{staff.view_info()}")
        else:
            self.menu.print_error(f"Staff with ID {staff_id} not found.")
    
    def update_staff_position(self):
        """Update staff position."""
        staff_id = self.menu.get_input("Enter staff ID: ")
        new_position = self.menu.get_input("Enter new position: ")
        result = self.staff_service.update_position(staff_id, new_position)
        if "updated" in result:
            self.menu.print_success(result)
        else:
            self.menu.print_error(result)
    
    def set_staff_schedule(self):
        """Set staff schedule."""
        staff_id = self.menu.get_input("Enter staff ID: ")
        schedule = self.menu.get_input("Enter schedule (e.g., Mon-Fri 9AM-5PM): ")
        result = self.staff_service.set_schedule(staff_id, schedule)
        if "set" in result:
            self.menu.print_success(result)
        else:
            self.menu.print_error(result)
    
    def department_management(self):
        """Handle department management."""
        while True:
            self.menu.display_department_menu()
            choice = self.menu.get_input()
            
            if choice == '1':
                self.create_department()
            elif choice == '2':
                self.view_department()
            elif choice == '3':
                self.add_patient_to_dept()
            elif choice == '4':
                self.add_staff_to_dept()
            elif choice == '5':
                depts = self.department_service.list_all_departments()
                if isinstance(depts, list):
                    print("\nDepartments:")
                    for d in depts:
                        print(f"  - {d}")
                else:
                    self.menu.print_info(depts)
            elif choice == '6':
                dept_code = self.menu.get_input("Enter department code to remove: ")
                result = self.hospital.remove_department(dept_code)
                if "removed" in result:
                    self.menu.print_success(result)
                else:
                    self.menu.print_error(result)
            elif choice == '0':
                break
            else:
                self.menu.print_error("Invalid choice. Please try again.")
    
    def create_department(self):
        """Create a new department."""
        name = self.menu.get_input("Enter department name: ")
        code = self.menu.get_input("Enter department code: ")
        dept = Department(name, code)
        result = self.department_service.create_department(dept)
        self.hospital.add_department(dept)
        self.menu.print_success(result)
    
    def view_department(self):
        """View department information."""
        dept_code = self.menu.get_input("Enter department code: ")
        result = self.department_service.get_department_info(dept_code)
        print(f"\n{result}")
    
    def add_patient_to_dept(self):
        """Add patient to department."""
        dept_code = self.menu.get_input("Enter department code: ")
        patient_id = self.menu.get_input("Enter patient ID: ")
        patient = self.patient_service.get_patient(patient_id)
        if patient:
            result = self.department_service.add_patient_to_department(dept_code, patient)
            if "added" in result:
                self.menu.print_success(result)
            else:
                self.menu.print_error(result)
        else:
            self.menu.print_error(f"Patient with ID {patient_id} not found.")
    
    def add_staff_to_dept(self):
        """Add staff to department."""
        dept_code = self.menu.get_input("Enter department code: ")
        staff_id = self.menu.get_input("Enter staff ID: ")
        staff = self.staff_service.get_staff_member(staff_id)
        if staff:
            result = self.department_service.add_staff_to_department(dept_code, staff)
            if "added" in result:
                self.menu.print_success(result)
            else:
                self.menu.print_error(result)
        else:
            self.menu.print_error(f"Staff with ID {staff_id} not found.")
    
    def view_system_status(self):
        """View system status."""
        while True:
            self.menu.display_status_menu()
            choice = self.menu.get_input()
            
            if choice == '1':
                info = self.hospital_service.get_hospital_info()
                print(f"\n{info}")
            elif choice == '2':
                total = self.patient_service.get_total_patients()
                print(f"\nTotal Patients: {total}")
            elif choice == '3':
                total = self.staff_service.get_total_staff()
                print(f"\nTotal Staff Members: {total}")
            elif choice == '4':
                total = self.department_service.get_total_departments()
                print(f"\nTotal Departments: {total}")
            elif choice == '5':
                beds = self.hospital_service.get_available_beds()
                print(f"\n{beds}")
            elif choice == '0':
                break
            else:
                self.menu.print_error("Invalid choice. Please try again.")
