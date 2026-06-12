no_of_std = int(input("Enter the student numer:"))
if no_of_std<2:
    print("number of student must be more than two")
else:
    student = []
    for i in range(no_of_std):
        std_name= input("Enter the student name{}:".format(i+1))
        std_marks = int(input("Enter the student marks{} :".format(i+1)))
        student.append([std_name,std_marks])
print(student)  
sorted_students = sorted(student, key = lambda item:item[1])
print(sorted_students)
second_lowest_grad = sorted_students[1][1]
grad1 = [student[0] for student in sorted_students if student[1] == second_lowest_grad ]

for item in grad1:
    print("-",item)

#2nd way
n1 = int(input("Enter the numer of student:"))

students = []
if n1<2:
    print("student count should be more than two")
else:
    for i in range(n1):
        stud1 = input("enter the student name:")
        marks = int(input("Enter the student marks:"))
        students.append([stud1,marks])
sorted_student = sorted(students, key = lambda x:x[1])      
print(sorted_student)
second_lowest= sorted_student[1][1]
print([student[0] for student in students if student[1] == second_lowest])