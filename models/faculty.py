class Faculty:
    def __init__(self, faculty_id, name, subjects, max_load, current_load):
        self.faculty_id = faculty_id
        self.name = name
        self.subjects = subjects
        self.max_load = max_load
        self.current_load = current_load
    
    def __str__(self):
        return f"Faculty ID : {self.faculty_id}\n\nName : {self.name}\n\nSubjects : {self.subjects}\n\nCurrent Load : {self.current_load}/{self.max_load}\n\n\n"

    def can_accept_load(self):
        return self.current_load < self.max_load
    
    def assign_lecture(self):
        if self.can_accept_load():
            self.current_load += 1
            return True
        else:
            return False
    
    def get_name(self):
        return self.name