l1 = [40,30,4,23,97,327,645,64,743,902,100,2]
l2 = l1.copy()
l3 = []
i=0
for i in range(len(l1)):
    for j in range(len(l1)):
        if l1[i]>l1[j]:
            pass
        else:
            l1[j],l1[i]=l1[i],l1[j]
print(l1)