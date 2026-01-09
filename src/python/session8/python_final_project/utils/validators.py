"""Validators for hospital system."""


class Validators:
    """Utility class for input validation."""
    
    @staticmethod
    def validate_email(email):
        """Validate email format."""
        return "@" in email and "." in email
    
    @staticmethod
    def validate_phone(phone):
        """Validate phone number."""
        return len(phone) >= 10 and phone.replace("-", "").replace(" ", "").isdigit()
    
    @staticmethod
    def validate_age(age):
        """Validate age."""
        try:
            age_int = int(age)
            return 0 <= age_int <= 150
        except ValueError:
            return False
    
    @staticmethod
    def validate_salary(salary):
        """Validate salary."""
        try:
            salary_float = float(salary)
            return salary_float >= 0
        except ValueError:
            return False
    
    @staticmethod
    def validate_id(id_str):
        """Validate ID format."""
        return len(id_str) > 0 and not " " in id_str
    
    @staticmethod
    def validate_name(name):
        """Validate name."""
        return len(name) > 0 and len(name) <= 100 and name.replace(" ", "").isalpha()
