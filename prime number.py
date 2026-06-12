def prime(num):
    for div in range(2,num):
        if num%div == 0:
            print(num ,"is not prime")
            break
    else:
        print(num, "is prime")

input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))
for num in range(input1,input2+1):
    prime(num)