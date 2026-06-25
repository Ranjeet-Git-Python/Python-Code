input1 = [0,9,0,7,0,11,0]
#and expected output should be - [0,0,0,0,9,7,11]

for i in range(len(input1)):
    if input1[i] == 0 :
        input1.insert(0,input1.pop(i))
print(input1)