"""Data manager for hospital system."""
import json
import os


class DataManager:
    """Utility class for managing data persistence."""
    
    def __init__(self, data_dir="data"):
        """
        Initialize DataManager.
        
        Args:
            data_dir (str): Directory to store data files
        """
        self.data_dir = data_dir
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
    
    def save_to_json(self, filename, data):
        """Save data to JSON file."""
        try:
            filepath = os.path.join(self.data_dir, filename)
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def load_from_json(self, filename):
        """Load data from JSON file."""
        try:
            filepath = os.path.join(self.data_dir, filename)
            if os.path.exists(filepath):
                with open(filepath, 'r') as f:
                    return json.load(f)
            return None
        except Exception as e:
            print(f"Error loading data: {e}")
            return None
    
    def save_hospitals(self, hospitals_data):
        """Save hospitals data."""
        return self.save_to_json("hospitals.json", hospitals_data)
    
    def load_hospitals(self):
        """Load hospitals data."""
        return self.load_from_json("hospitals.json")
    
    def save_patients(self, patients_data):
        """Save patients data."""
        return self.save_to_json("patients.json", patients_data)
    
    def load_patients(self):
        """Load patients data."""
        return self.load_from_json("patients.json")
    
    def save_staff(self, staff_data):
        """Save staff data."""
        return self.save_to_json("staff.json", staff_data)
    
    def load_staff(self):
        """Load staff data."""
        return self.load_from_json("staff.json")
    
    def save_departments(self, departments_data):
        """Save departments data."""
        return self.save_to_json("departments.json", departments_data)
    
    def load_departments(self):
        """Load departments data."""
        return self.load_from_json("departments.json")
