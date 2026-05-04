#Question: Basic dictionary operations
student = {"name": "Alice", "age": 20, "grade": "B"}

#Output: {"name": "Alice", "age": 21, "grade": "B", "city": "New York"} and Name: Alice
#student["age"]=21
student.update(age=21,city= "New York")
print(student)
print("Name:",student["name"])