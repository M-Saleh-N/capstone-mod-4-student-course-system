# tests/test_enrollment.py

import unittest
import sys
import os

# ✅ Allow import from the main project directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from course import Course
from student import Student

class TestStudentCourseManagement(unittest.TestCase):

    def setUp(self):
        """
        Set up a test student and sample courses before each test.
        """
        # Create a fake database-like object for the Student class to use
        mock_db = type('MockDB', (), {
            'id': 1,
            'name': 'Test Student',
            'email': 'test@example.com',
            'courses': []
        })

        self.student = Student(mock_db())
        self.python = Course(101, "Intro to Python", "Dr. Smith", 3)
        self.ds = Course(102, "Data Structures", "Prof. Alice", 4)

    def test_enroll_course(self):
        """
        Test if a student can enroll in a course.
        """
        self.student.enroll(self.python)
        history = self.student.course_history.list_courses()
        self.assertIn("Intro to Python [101]", history[0])

    def test_drop_existing_course(self):
        """
        Test dropping a course that exists in the student's history.
        """
        self.student.enroll(self.ds)
        self.student.drop(102)
        history = self.student.course_history.list_courses()
        self.assertNotIn("Data Structures [102]", "".join(history))

    def test_drop_nonexistent_course(self):
        """
        Test trying to drop a course that doesn't exist.
        """
        result = self.student.course_history.remove_course(999)
        self.assertFalse(result)

    def test_view_courses_empty(self):
        """
        Test viewing courses when student hasn't enrolled in any.
        """
        self.assertEqual(self.student.course_history.list_courses(), [])

if __name__ == '__main__':
    unittest.main()
