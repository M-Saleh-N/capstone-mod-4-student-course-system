from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Define the base class for all models
Base = declarative_base()

engine = create_engine("sqlite:///student_courses.db", echo=False)


SessionLocal = sessionmaker(bind=engine)
