class Course:
    def __init__(self, course_id, name, instructor, credits):
        self.course_id = course_id
        self.name = name
        self.instructor = instructor
        self.credits = credits

    def __str__(self):
        return f"{self.name} [{self.course_id}] - {self.instructor}, {self.credits} cr"
