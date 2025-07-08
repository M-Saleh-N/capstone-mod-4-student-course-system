from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base
from models.enrollment import enrollment_table

class StudentModel(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    courses = relationship("CourseModel", secondary=enrollment_table, back_populates="students")

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', email='{self.email}')>"
