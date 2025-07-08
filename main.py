from models.base import Base, engine, SessionLocal
from models.student_model import StudentModel
from models.course_model import CourseModel

from student import Student  # your OOP class
import os

if not os.path.exists("student_courses.db"):
    Base.metadata.create_all(bind=engine)

session = SessionLocal()

course_data = [
    ("Intro to Python", "Dr. Smith", 3),
    ("Data Structures", "Prof. Alice", 4),
    ("Databases", "Dr. Lee", 3),
]

courses = []
for name, instructor, credits in course_data:
    course = session.query(CourseModel).filter_by(name=name).first()
    if not course:
        course = CourseModel(name=name, instructor=instructor, credits=credits)
        session.add(course)
        session.commit()
    courses.append(course)

student_db = session.query(StudentModel).filter_by(email="saleh@example.com").first()
if not student_db:
    student_db = StudentModel(name="Saleh Mohamed", email="saleh@example.com")
    session.add(student_db)
    session.commit()

for course in courses:
    if course not in student_db.courses:
        student_db.courses.append(course)
session.commit()

student = Student(student_db)
student.view_courses()

session.close()

