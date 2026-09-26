from student import Student
from course import Course
from utils import print_heading, calculate_course_fee


def main():
    print_heading("Python Learning Platform")

    student = Student(
        student_id=101,
        name="Ramu",
        course="Python Programming"
    )

    course = Course(
        course_id="PY101",
        course_name="Python Programming",
        instructor="John"
    )

    student.display()
    course.display()

    fee = calculate_course_fee(10000, 10)

    print(f"Course Fee after discount: ₹{fee:.2f}")


if __name__ == "__main__":
    main()