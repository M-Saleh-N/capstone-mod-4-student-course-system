from sqlalchemy import Table, Column, Integer, ForeignKey
from models.base import Base

enrollment_table = Table(
    "enrollments",         # Table name
    Base.metadata,         # Link to the shared Base
    Column("student_id", Integer, ForeignKey("students.id")),
    Column("course_id", Integer, ForeignKey("courses.id"))
)
