from models.faculty import Faculty
from models.subject import Subject

f1 = Faculty("F101", "Dr. Sharma", ["DBMS", "CN"], 16, 8)
f2 = Faculty("F102", "Dr. Verma", ["DBMS", "CN"], 16, 8)
s1 = Subject("IT101", "Data Structures and Algorithms", f1, 4, 2, 5)
s2 = Subject("IT102", "Database Management System", f2, 4, 2, 5)
print(s1.display_info())
print(s2.display_info())