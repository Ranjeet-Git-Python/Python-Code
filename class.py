#Question: Create a class with class attributes and instance attributes, and demonstrate how to access them.
class Student: 
    # Class attribute
    school_name = "ABC School"

    def __init__(self, student_id, student_name, class_name):
        self.student_id = student_id
        self.student_name = student_name
        self.class_name = class_name 
student = Student('V12', 'Frank Gibson', 'V')
print(student.__dict__)
print(student.school_name)  # Accessing class attribute