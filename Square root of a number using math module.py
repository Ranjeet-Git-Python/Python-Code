#Question 6. Square root of a number using math module
import math
input1 = input("enter number as string:")
l1=input1.split(",")
l2=[]
c=50
h= 30
for i in l1:
    Q=math.sqrt((2*c*int(i))/h)
    l2.append(str(int(Q)))

print(",".join(l2))