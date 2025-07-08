class CourseHistoryNode:
    def __init__(self, course):
        self.course = course
        self.next = None

class CourseHistoryLinkedList:
    def __init__(self):
        self.head = None

    def add_course(self, course):
        new_node = CourseHistoryNode(course)
        new_node.next = self.head
        self.head = new_node

    def remove_course(self, course_id):
        current = self.head
        prev = None
        while current:
            if current.course.course_id == course_id:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def list_courses(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.course))
            current = current.next
        return result
