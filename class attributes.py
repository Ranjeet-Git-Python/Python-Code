class Student: 
    def __init__(self, student_id, student_name, class_name):
        self.student_id = student_id
        self.student_name = student_name
        self.class_name = class_name 
student = Student('V12', 'Frank Gibson', 'V')
print(student.__dict__)
print(student.student_id)
print(student.student_name)
print(student.class_name)
print(Student.__dict__)
print(Student.__name__)
print(Student.__module__)
print(Student.__bases__)
print(Student.__doc__)
print(Student.__init__)