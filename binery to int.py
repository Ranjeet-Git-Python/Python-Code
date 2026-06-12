input1 = input("Enter the binary number:")
l1 = input1.split(",")
l2=[]
for i in l1:
    x = int(i,2) #converts binary to  int(i,8) for octal and int(i,16) for hexadecimal
    if x%5==0:
        l2.append(i)
print(",".join(l2))