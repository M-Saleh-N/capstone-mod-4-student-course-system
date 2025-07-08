# 🎓 Student Course Management System

This is a Capstone Project built with Python and SQLAlchemy.  
It simulates a basic student-course enrollment system using:

- ✅ Object-Oriented Programming (OOP)
- 🔗 A Linked List to track course history
- 🗄️ SQLAlchemy ORM for persistent storage
- 🧪 Unit Testing with `unittest`

---

## 💡 Features

- 👨‍🎓 OOP Design for `Student` and `Course`
- 🔁 Custom Linked List to maintain course enrollment history
- 🗃️ SQLite database (`student_courses.db`) via SQLAlchemy
- ✅ Unit tests for core logic (enroll, drop, list)
- 🧱 Clean and beginner-friendly codebase

---

## 🏗️ Folder Structure

student-course-system/
│
├── course.py # Course class (OOP)
├── course_history.py # Linked List class
├── student.py # Student logic using Linked List
├── main.py # Runs demo with DB
│
├── models/ # SQLAlchemy ORM files
│ ├── base.py # DB engine and session setup
│ ├── course_model.py # ORM Course table
│ ├── student_model.py # ORM Student table
│ └── enrollment.py # Join table (students ↔ courses)
│
├── tests/ # Unit tests
│ └── test_enrollment.py # Tests for enrollment logic
│
├── requirements.txt # Python dependencies
└── README.md # Project overview and usage

yaml
Copy code

---

## ⚙️ How to Run

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
2️⃣ Run the application
bash
Copy code
python main.py
3️⃣ Run unit tests
bash
Copy code
python -m unittest discover tests
📁 Database
Uses SQLite database: student_courses.db

Created automatically on first run

Stores: students, courses, and their enrollments

📦 Dependencies
Add these in your requirements.txt:

text
Copy code
SQLAlchemy==2.0.30
📋 Sample Output
text
Copy code
Courses for Saleh Mohamed:
- Databases [103] - Dr. Lee, 3 cr
- Data Structures [102] - Prof. Alice, 4 cr
- Intro to Python [101] - Dr. Smith, 3 cr
👨‍💻 Author
Saleh Mohamed