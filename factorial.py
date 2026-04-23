input_no = int(input("Enter any number: "))
factorial = 1
for i in range(1, input_no + 1):
    factorial *= i
print("The factorial of", input_no, "is:", factorial)

# 2nd method
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

input_no = int(input("Enter any number: "))
print("The factorial of", input_no, "is:", factorial(input_no))

#3rd method

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
input_no = int(input("Enter any number: "))
print("The factorial of", input_no, "is:", factorial(input_no))
