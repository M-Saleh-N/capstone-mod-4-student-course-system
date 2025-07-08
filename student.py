from course_history import CourseHistoryLinkedList

class Student:
    def __init__(self, db_instance):
        """
        Initialize using a StudentModel instance from the database.
        """
        self.student_id = db_instance.id
        self.name = db_instance.name
        self.email = db_instance.email
        self.course_history = CourseHistoryLinkedList()

        # Load enrolled courses from DB into the linked list
        for course in db_instance.courses:
            self.course_history.add_course(course)

    def enroll(self, course):
        self.course_history.add_course(course)
        print(f"{self.name} enrolled in {course.name}.")

    def drop(self, course_id):
        success = self.course_history.remove_course(course_id)
        if success:
            print(f"{self.name} dropped course ID {course_id}.")
        else:
            print(f"Course ID {course_id} not found for {self.name}.")

    def view_courses(self):
        print(f"\nCourses for {self.name}:")
        courses = self.course_history.list_courses()
        if not courses:
            print("No courses enrolled yet.")
        for course in courses:
            print(f"- {course}")
