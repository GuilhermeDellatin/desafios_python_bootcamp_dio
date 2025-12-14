class Student:
    school = "Harvard University"

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self) -> str:
        return f"{self.name} - {self.number} - {self.school}"

def show_student(*objects):
    for obj in objects:
        print(obj)

student_1 = Student(name="Guilherme", number=1)
student_2 = Student(name="Camila", number=2)

show_student(student_1, student_2)

Student.school = "Oxford University"

student_3 = Student(name="Amélia", number=3)
student_3.school = "Harvard University"
show_student(student_1, student_2, student_3)

