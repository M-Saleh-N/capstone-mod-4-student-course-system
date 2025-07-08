from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base
from models.enrollment import enrollment_table

class CourseModel(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    instructor = Column(String, nullable=False)
    credits = Column(Integer, nullable=False)

    students = relationship("StudentModel", secondary=enrollment_table, back_populates="courses")

    def __repr__(self):
        return f"<Course(id={self.id}, name='{self.name}', instructor='{self.instructor}', credits={self.credits})>"
