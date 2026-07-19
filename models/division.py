from .subject import Subject
class Division:
    def __init__(self, division_id, division_name, semester, branch, student_count, faculty_incharge, subjects = None):
        self.division_id = division_id
        self.division_name = division_name
        self.semester = semester
        self.branch = branch
        self.student_count = student_count
        self.faculty_incharge = faculty_incharge
        if subjects is None:
            self.subjects = []
        else:
            self.subjects = subjects
    
    def __str__(self):
        return f"Division ID : {self.division_id}\nDivision Name : {self.division_name}\nSemester : {self.semester}\nBranch : {self.branch}\nStudent Count : {self.student_count}\nFaculty Incharge : {self.faculty_incharge}\nSubjects : {self.subjects}"
    
    def add_subject(self, subject):
        if isinstance(subject, Subject):
            self.subjects.append(subject)
            return True
        else:
            return False