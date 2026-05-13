#Question: Given a list of integers, replace all occurrences of the number 1 with the number 9 and print the modified list.
list1 = [2,1,3,1,1,4,5,1,3,1]
#list1 = [9 if i==1 else i for i in list1]
list1 = [i for i in list1 if i==1 else 9]
print(list1)