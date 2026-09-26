class Student:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def display(self):
        print(
            f"ID: {self.student_id}, "
            f"Name: {self.name}, "
            f"Course: {self.course}"
        )