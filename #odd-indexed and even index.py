#odd-indexed elements from the first list and even-indexed elements from the second# Outputs: "fl"
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l1_odd = []
l2_even = []
for i in range(max(len(l1),len(l2))):
    if i % 2 != 0:
        l1_odd.append(l1[i])
    else:
        l2_even.append(l2[i])

print(l1_odd+l2_even)   

#2nd way
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
res = list()

odd_elements = list1[1::2]
print("Element at odd-index positions from list one")
print(odd_elements)

even_elements = list2[0::2]
print("Element at even-index positions from list two")
print(even_elements)

print("Printing Final third list")
res.extend(odd_elements)
res.extend(even_elements)
print(res)

#Slice list into 3 equal chunks and reverse each chunk
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
l1 = []
l2 = []
l3 = []
for i in range(len(sample_list)):
    if i < 3:
        l1.append(sample_list[i])
    elif i>=3 and i <6:
        l2.append(sample_list[i])
    else:
        l3.append(sample_list[i])
print("Chunk 1" , l1)
print("After reversing it: " , l1[::-1])
print("Chunk 2", l2)
print("After reversing it: " , l2[::-1])
print("Chunk 3", l3)
print("After reversing it: ", l3[::-1])

#shows the element from both lists in a pair.
first_list = [2, 3, 4, 5, 6, 7, 8]
print("First List ", first_list)

second_list = [4, 9, 16, 25, 36, 49, 64]
print("Second List ", second_list)

result = zip(first_list, second_list)
result_set = set(result)
print(result_set)     

#Set Intersection and Removal
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
int_set = first_set.intersection(second_set)
print("Intersection of the two sets is ", int_set)

diff_set = first_set.difference(second_set)
print("Difference of the two sets is ", diff_set)

print("Intersection is ", int_set)
for item in int_set:
    first_set.remove(item)
print("First Set after removing common element ", first_set)

#Extract Unique Dictionary Values to List
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
#output [47, 52, 44, 53, 54]
list1 = []
values = speed.values()
for i in values:
    if i not in  list1:
        list1.append(i)
print(list1)