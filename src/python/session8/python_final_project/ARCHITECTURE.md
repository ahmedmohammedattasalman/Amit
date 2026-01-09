"""
HOSPITAL MANAGEMENT SYSTEM - PIPELINE ARCHITECTURE
====================================================

PROJECT STRUCTURE OVERVIEW
==========================

┌─────────────────────────────────────────────────────────────┐
│                     USER INTERFACE LAYER (UI)               │
│   MenuSystem + HospitalUI - Interactive Menu System         │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                    SERVICES LAYER                           │
│  HospitalService │ PatientService │ StaffService │ DeptSvc  │
│  Business Logic & Data Processing                           │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                     MODELS LAYER                            │
│  Person │ Patient │ Staff │ Department │ Hospital           │
│  Data Structures & Core Entities                            │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                   UTILITIES LAYER                           │
│        Validators │ DataManager │ Configuration             │
│  Helper Functions & Data Persistence                        │
└─────────────────────────────────────────────────────────────┘


DATA FLOW PIPELINE
==================

User Input (UI) 
    ↓
Menu Selection
    ↓
Route to Service
    ↓
Service uses Models
    ↓
Business Logic Execution
    ↓
Return Results
    ↓
Display to User


FEATURES BY LAYER
=================

MODELS (Data Layer)
-------------------
✓ Person - Base class for all people
✓ Patient - Extends Person with medical records
✓ Staff - Extends Person with position/schedule
✓ Department - Manages patients and staff
✓ Hospital - Top-level entity managing departments

SERVICES (Business Logic Layer)
-------------------------------
✓ HospitalService - Hospital operations
✓ PatientService - Patient management (register, update, track)
✓ StaffService - Staff management (hire, schedule, remove)
✓ DepartmentService - Department operations

UI (Presentation Layer)
-----------------------
✓ MenuSystem - Display menus and get input
✓ HospitalUI - Coordinate user interactions
✓ Interactive menus for each module
✓ Error handling and user feedback

UTILITIES (Support Layer)
------------------------
✓ Validators - Input validation
✓ DataManager - Data persistence (JSON)
✓ Configuration - Centralized settings


KEY CLASSES & METHODS
====================

Person:
  - __init__(name, age, id_number)
  - view_info()

Patient (inherits Person):
  - update_record(new_record)
  - update_status(status)
  - view_record()

Staff (inherits Person):
  - set_schedule(schedule)
  - get_schedule()

Department:
  - add_patient(patient)
  - add_staff(staff_member)
  - get_patients_count()
  - get_staff_count()

Hospital:
  - add_department(department)
  - get_department(code)
  - set_total_beds(total)
  - occupy_bed()
  - free_bed()

PatientService:
  - register_patient(patient)
  - get_patient(patient_id)
  - update_patient_record(patient_id, record)
  - update_patient_status(patient_id, status)
  - list_all_patients()

StaffService:
  - hire_staff(staff_member)
  - get_staff_member(staff_id)
  - update_position(staff_id, position)
  - set_schedule(staff_id, schedule)
  - list_all_staff()

DepartmentService:
  - create_department(department)
  - get_department(code)
  - add_patient_to_department(code, patient)
  - add_staff_to_department(code, staff)
  - list_all_departments()

HospitalUI:
  - run() - Main application loop
  - hospital_operations()
  - patient_management()
  - staff_management()
  - department_management()
  - view_system_status()


USAGE EXAMPLE
=============

from models import Hospital, Patient, Staff, Department
from services import PatientService, HospitalService
from ui import HospitalUI

# Create hospital
hospital = Hospital("City Medical Center", "123 Ave", "555-0100", "info@hospital.com")
hospital.set_total_beds(500)

# Add departments
cardiology = Department("Cardiology", "CARD")
hospital.add_department(cardiology)

# Create service
patient_service = PatientService()

# Register patient
patient = Patient("Alice", 30, "PAT001", "No allergies")
patient_service.register_patient(patient)

# Start UI
ui = HospitalUI(hospital)
ui.run()


FEATURES IMPLEMENTED
====================

Hospital Operations:
  ✓ View hospital information
  ✓ List all departments
  ✓ Check available beds
  ✓ Manage bed allocation

Patient Management:
  ✓ Register new patients
  ✓ View patient information
  ✓ Update medical records
  ✓ Change patient status
  ✓ List all patients
  ✓ Remove patients

Staff Management:
  ✓ Hire new staff members
  ✓ View staff information
  ✓ Update staff positions
  ✓ Set work schedules
  ✓ List staff by position/department
  ✓ Remove staff members

Department Management:
  ✓ Create departments
  ✓ Add/remove patients
  ✓ Add/remove staff
  ✓ View department info
  ✓ Track resources

System Status:
  ✓ Hospital overview
  ✓ Patient count
  ✓ Staff count
  ✓ Department count
  ✓ Bed availability


EXTENSIBILITY GUIDELINES
=========================

To add a new feature:

1. Add Model (if needed):
   - Create class in models/
   - Follow Person inheritance pattern

2. Create Service:
   - Create service in services/
   - Implement CRUD operations

3. Add UI Methods:
   - Add methods in hospital_ui.py
   - Add menu display in menu_system.py

4. Update Configuration:
   - Add to config.py if needed

5. Test the Feature:
   - Test through interactive UI


DESIGN PATTERNS USED
====================

1. Pipeline Architecture
   - Organized layers with clear flow
   - Each layer processes and passes data

2. Service Pattern
   - Separates business logic from UI
   - Reusable services across UIs

3. MVC-like Pattern
   - Models (data)
   - Services (logic)
   - UI (presentation)

4. Factory Pattern
   - Service creation
   - Object initialization

5. Singleton Pattern
   - Single hospital instance
   - Single service instances

6. Strategy Pattern
   - Different operations strategies
   - Pluggable behavior


FILE LOCATIONS
==============

python_final_project/
├── models/
│   ├── __init__.py
│   ├── person.py          (Person base class)
│   ├── patient.py         (Patient class with inheritance)
│   ├── staff.py           (Staff class with inheritance)
│   ├── department.py      (Department management)
│   └── hospital.py        (Hospital management)
├── services/
│   ├── __init__.py
│   ├── hospital_service.py (Hospital operations)
│   ├── patient_service.py  (Patient operations)
│   ├── staff_service.py    (Staff operations)
│   └── department_service.py (Department operations)
├── ui/
│   ├── __init__.py
│   ├── menu_system.py     (Menu display/input)
│   └── hospital_ui.py     (Main UI controller)
├── utils/
│   ├── __init__.py
│   ├── validators.py      (Input validation)
│   └── data_manager.py    (Data persistence)
├── main.py                (Entry point)
├── config.py              (Configuration)
├── __init__.py            (Package init)
├── requirements.txt       (No external dependencies)
└── README.md              (Documentation)


RUNNING THE SYSTEM
==================

1. Navigate to python_final_project directory
2. Run: python main.py
3. Follow the interactive menu system
4. Use number keys to select operations
5. Follow prompts to enter data
6. View results and navigate using menu


VALIDATION & ERROR HANDLING
============================

✓ Input validation in Validators class
✓ Try-catch blocks in main.py
✓ Graceful error messages in services
✓ User-friendly error feedback in UI
✓ Prevents duplicate entries
✓ Checks for missing records


FUTURE ENHANCEMENTS
===================

1. Database Integration
   - Replace dict storage with SQL database
   - Add persistence across sessions

2. Authentication
   - User login system
   - Role-based access control

3. Reporting
   - Generate hospital reports
   - Statistical analysis
   - Patient/Staff reports

4. Advanced Scheduling
   - Shift management
   - Conflict resolution
   - Calendar view

5. Billing System
   - Patient billing
   - Invoice generation
   - Payment tracking

6. Medical Records
   - Detailed medical history
   - Lab results storage
   - Prescription management

7. Web Interface
   - REST API
   - Web dashboard
   - Mobile app

8. Notifications
   - Email alerts
   - SMS notifications
   - Appointment reminders
"""
