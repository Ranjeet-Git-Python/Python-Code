list1 = ['l1','l2','l3','l1','l2']
l1 = []
for i in list1:
  if list1.count(i)>1 and i not in l1:
    l1.append(i)

print(l1)
    
    
    