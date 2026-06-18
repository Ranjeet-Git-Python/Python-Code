input1 =  "1,3,4,3-5,4,6,5-9,2,3,4"
#output: [1,3,4,3,4,5,4,6,5,6,7,8,9,2,3,4]
data = input1.split(",")
list1 = []
for i in data:
    if "-" in i:
        data2 = i.split("-")
        for j in range(int(data2[0]),int(data2[1])+1):
            list1.append(j)
    else:
        list1.append(int(i))
print(list1)