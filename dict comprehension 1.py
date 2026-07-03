# dict comprehension
list1 = [2, 3, 5, 7, 11]
squared_dict = {x:x**2 for x in list1}
print(squared_dict)
print(type(squared_dict))
# output is {11: 121, 2: 4 , 3: 9 , 5: 25 , 7: 49}