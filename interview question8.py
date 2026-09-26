#find missing values
list1 = [2,3,5,8,11]
max1 = max(list1)
min1 = min(list1)
l1 = []
for i in range(min1, max1+1):
  if i not in list1:
    l1.append(i)
print(l1)
    