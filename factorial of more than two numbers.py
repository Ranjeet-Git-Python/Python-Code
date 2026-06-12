def fac(num):
    if num == 1:
        return 1
    else:
        return num*fac(num-1)
#print(fac(5))
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
result = []
for i in range(num1,num2+1):
    result.append(fac(i))
print(result)