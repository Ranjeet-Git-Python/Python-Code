#Question: Write a Python program to generate the Fibonacci sequence up to the 10th term.
num = [0,1]
i=0
while i<10:
    num_add = num[-1]+num[-2]
    num.append(num_add)
    i+=1
print(num)


num = [0,1]
n= 10
for i in range(2,n+1):
    num_add = num[-1]+num[-2]
    num.append(num_add)
print(num)