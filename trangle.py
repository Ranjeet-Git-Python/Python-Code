#Question: Write a Python program to print a triangle pattern of numbers based on user input. The program should take an integer n as input and print a triangle with n rows, where the i-th row contains the number i repeated i times, separated by spaces.
n = int(input("Enter n: "))

# for i in range(1, n + 1):
#     leading = " " * ((n - i) * 2)
#     between = " " * ((i - 1) * 2)
#     print(leading + between.join([str(i)] * i))

# 2nd method
for i in range(1, n + 1):
    print(((10 ** (i)) // 9) *  i)