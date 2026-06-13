
#Question: Write a Python program to calculate the factorial of a given number.
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

#question 2: Factorial of a number using recursion and iteration
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
l1 =[]
p= 1
for i in range(num1,num2+1):
    for j in range(1,i+1):
        p=j*p
    l1.append(str(p))
    p=1
str2=",".join(l1)
print(str2)
#2nd way
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
        
p=fact(4)
print(p)
#Question 3. factorial of a number using recursion and iteration between two numbers
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
l1 =[]
p= 1
for i in range(num1,num2+1):
    p=fact(i)
    l1.append(str(p))
    p=1
str2=",".join(l1)
print(str2)