from .faculty import Faculty

class Subject:
    def __init__(self, subject_id, subject_name, faculty, weekly_lectures, weekly_practicals = 0, credits = 0):
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.faculty = faculty
        self.weekly_lectures = weekly_lectures
        self.weekly_practicals = weekly_practicals
        self.credits = credits
    
    def display_info(self):
        return f"Subject ID : {self.subject_id}\nSubject Name : {self.subject_name}\nFaculty : {self.faculty.get_name()}\nWeekly Lectures : {self.weekly_lectures}\nWeekly Practicals : {self.weekly_practicals}\nCredits : {self.credits}\n\n"