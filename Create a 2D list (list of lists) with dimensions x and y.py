#Question 7. Create a 2D list (list of lists) with dimensions x and y, 
# where each element is the product of its indices.
x=3
y=5
l2=[]
for i in range(x):
    l1=[]
    for j in range(y):
        l1.append(i*j)
    l2.append(l1)
print(l2)