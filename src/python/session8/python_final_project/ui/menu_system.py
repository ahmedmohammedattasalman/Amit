"""Menu system for hospital application."""


class MenuSystem:
    """Menu system for user interaction."""
    
    @staticmethod
    def display_main_menu():
        """Display main menu."""
        print("\n" + "="*50)
        print("       HOSPITAL MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Hospital Operations")
        print("2. Patient Management")
        print("3. Staff Management")
        print("4. Department Management")
        print("5. View System Status")
        print("0. Exit")
        print("="*50)
    
    @staticmethod
    def display_hospital_menu():
        """Display hospital operations menu."""
        print("\n" + "-"*50)
        print("       HOSPITAL OPERATIONS")
        print("-"*50)
        print("1. View Hospital Info")
        print("2. List All Departments")
        print("3. View Available Beds")
        print("4. Occupy a Bed")
        print("5. Free a Bed")
        print("0. Back to Main Menu")
        print("-"*50)
    
    @staticmethod
    def display_patient_menu():
        """Display patient management menu."""
        print("\n" + "-"*50)
        print("       PATIENT MANAGEMENT")
        print("-"*50)
        print("1. Register New Patient")
        print("2. View Patient Info")
        print("3. Update Patient Record")
        print("4. Update Patient Status")
        print("5. List All Patients")
        print("6. Remove Patient")
        print("0. Back to Main Menu")
        print("-"*50)
    
    @staticmethod
    def display_staff_menu():
        """Display staff management menu."""
        print("\n" + "-"*50)
        print("       STAFF MANAGEMENT")
        print("-"*50)
        print("1. Hire New Staff")
        print("2. View Staff Info")
        print("3. Update Staff Position")
        print("4. Set Staff Schedule")
        print("5. List All Staff")
        print("6. Remove Staff")
        print("0. Back to Main Menu")
        print("-"*50)
    
    @staticmethod
    def display_department_menu():
        """Display department management menu."""
        print("\n" + "-"*50)
        print("       DEPARTMENT MANAGEMENT")
        print("-"*50)
        print("1. Create Department")
        print("2. View Department Info")
        print("3. Add Patient to Department")
        print("4. Add Staff to Department")
        print("5. List All Departments")
        print("6. Remove Department")
        print("0. Back to Main Menu")
        print("-"*50)
    
    @staticmethod
    def display_status_menu():
        """Display system status menu."""
        print("\n" + "-"*50)
        print("       SYSTEM STATUS")
        print("-"*50)
        print("1. Hospital Status")
        print("2. Total Patients")
        print("3. Total Staff")
        print("4. Total Departments")
        print("5. Bed Status")
        print("0. Back to Main Menu")
        print("-"*50)
    
    @staticmethod
    def get_input(prompt="Enter choice: "):
        """Get user input safely."""
        try:
            return input(prompt).strip()
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return "0"
    
    @staticmethod
    def print_separator():
        """Print a visual separator."""
        print("-"*50)
    
    @staticmethod
    def print_success(message):
        """Print success message."""
        print(f"✓ {message}")
    
    @staticmethod
    def print_error(message):
        """Print error message."""
        print(f"✗ {message}")
    
    @staticmethod
    def print_info(message):
        """Print info message."""
        print(f"ℹ {message}")
