# Get number of students
n = int(input("Enter number of students: "))

# Create nested list to store [name, grade] for each student
students = []

for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    grade = float(input(f"Enter grade of student {i+1}: "))
    students.append([name, grade])

print("\nStudent List:")
print(students)

# Find second lowest grade
if len(students) < 2:
    print("Need at least 2 students to find second lowest grade")
else:
    # Sort by grade (index 1)
    sorted_students = sorted(students, key=lambda x: x[1])
    
    # Get the second lowest grade
    second_lowest_grade = sorted_students[1][1]
    
    # Find all students with second lowest grade
    students_with_second_lowest = [student[0] for student in sorted_students if student[1] == second_lowest_grade]
    
    print(f"\nStudent(s) with second lowest grade ({second_lowest_grade}):")
    for student_name in students_with_second_lowest:
        print(f"  - {student_name}")

# 2nd method
grades = [student[1] for student in students]
unique_grades = sorted(set(grades))
if len(unique_grades) < 2:
    print("Need at least 2 unique grades to find second lowest grade")
else:
    second_lowest_grade = unique_grades[1]
    stude_second_lowestnts_with = [student[0] for student in students if student[1] == second_lowest_grade]
    
    print(f"\nStudent(s) with second lowest grade ({second_lowest_grade}):")
    for student_name in students_with_second_lowest:
        print(f"  - {student_name}")
    