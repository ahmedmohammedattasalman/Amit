"""Staff service for managing staff operations."""


class StaffService:
    """Service class for staff operations."""
    
    def __init__(self):
        """Initialize StaffService."""
        self.staff_members = {}
    
    def hire_staff(self, staff_member):
        """Hire a new staff member."""
        if staff_member.id_number not in self.staff_members:
            self.staff_members[staff_member.id_number] = staff_member
            return f"Staff member {staff_member.name} hired successfully."
        return f"Staff member with ID {staff_member.id_number} already exists."
    
    def get_staff_member(self, staff_id):
        """Get staff member by ID."""
        return self.staff_members.get(staff_id, None)
    
    def update_position(self, staff_id, new_position):
        """Update staff member position."""
        if staff_id in self.staff_members:
            staff = self.staff_members[staff_id]
            staff.position = new_position
            return f"Position updated to {new_position} for {staff.name}."
        return f"Staff member with ID {staff_id} not found."
    
    def set_schedule(self, staff_id, schedule):
        """Set staff member schedule."""
        if staff_id in self.staff_members:
            staff = self.staff_members[staff_id]
            return staff.set_schedule(schedule)
        return f"Staff member with ID {staff_id} not found."
    
    def remove_staff(self, staff_id):
        """Remove staff member from system."""
        if staff_id in self.staff_members:
            staff = self.staff_members.pop(staff_id)
            return f"Staff member {staff.name} removed from system."
        return f"Staff member with ID {staff_id} not found."
    
    def list_all_staff(self):
        """List all staff members."""
        if not self.staff_members:
            return "No staff members registered."
        return [staff.view_info() for staff in self.staff_members.values()]
    
    def get_staff_by_position(self, position):
        """Get staff members by position."""
        result = [s for s in self.staff_members.values() if s.position == position]
        return result if result else f"No staff members with position '{position}'."
    
    def get_staff_by_department(self, department):
        """Get staff members by department."""
        result = [s for s in self.staff_members.values() if s.department == department]
        return result if result else f"No staff members in {department} department."
    
    def get_total_staff(self):
        """Get total number of staff members."""
        return len(self.staff_members)
