"""
README - Hospital Management System
====================================

## Project Structure

This is a well-organized pipeline-based Hospital Management System with the following architecture:

### Folder Structure:
```
python_final_project/
├── models/              # Data models (Person, Patient, Staff, Department, Hospital)
├── services/            # Business logic layer (HospitalService, PatientService, StaffService, DepartmentService)
├── ui/                  # User interface (MenuSystem, HospitalUI)
├── utils/               # Utilities (Validators, DataManager)
├── main.py             # Entry point
├── config.py           # Configuration
└── README.md           # This file
```

## Pipeline Architecture

The system follows a **layered pipeline architecture**:

1. **Models Layer** (`models/`)
   - Defines data structures
   - Contains Person, Patient, Staff, Department, Hospital classes
   - Each model has its own file for modularity

2. **Services Layer** (`services/`)
   - Contains business logic
   - HospitalService - manages hospital operations
   - PatientService - manages patient records
   - StaffService - manages staff
   - DepartmentService - manages departments

3. **UI Layer** (`ui/`)
   - MenuSystem - handles menu display and user input
   - HospitalUI - orchestrates user interactions
   - Routes user commands to appropriate services

4. **Utilities Layer** (`utils/`)
   - Validators - validates input data
   - DataManager - handles data persistence

## Features

### Hospital Operations
- View hospital information
- Manage departments
- Track available beds
- Occupy and free beds

### Patient Management
- Register new patients
- View patient information
- Update medical records
- Change patient status (Active, Discharged, Critical, etc.)
- Remove patients from system

### Staff Management
- Hire new staff members
- Update staff positions
- Set work schedules
- Remove staff members
- List staff by position or department

### Department Management
- Create new departments
- Add patients to departments
- Add staff to departments
- View department information
- Remove departments

## How to Run

1. Navigate to the python_final_project directory
2. Run the main.py file:
   ```
   python main.py
   ```
3. Follow the on-screen menu to navigate the system

## Example Usage

The system starts with a pre-configured hospital "City Medical Center" with 5 departments:
- Cardiology
- Emergency
- Orthopedics
- Neurology
- Pediatrics

You can then:
- Register patients
- Hire staff
- Assign them to departments
- Manage their information

## Key Design Patterns

1. **Separation of Concerns** - Each layer handles specific responsibilities
2. **Pipeline Pattern** - Data flows through organized layers
3. **Single Responsibility** - Each class has one clear purpose
4. **Modularity** - Easy to add new features without affecting existing code
5. **Service Layer** - Business logic separated from UI

## Extensibility

To add new features:
1. Add new models in `models/` if needed
2. Create corresponding service in `services/`
3. Add UI methods in `ui/hospital_ui.py`
4. Add menu options in `ui/menu_system.py`

## Error Handling

The system includes:
- Input validation
- Error messages for invalid operations
- Exception handling in main.py
- Graceful error handling in all services
"""
