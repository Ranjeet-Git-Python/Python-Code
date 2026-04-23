num = [0,1]
num1=[0]
i=0
while i<10:
    num_add = num[-1]+num[-2]
    num.append(num_add)
    num1.append(num_add)
    i+=1
print(num1)