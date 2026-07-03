from copy import copy, deepcopy

list_1 = [1, 2, [3, 5], 4]
# shallow
list_2 = copy(list_1)
list_2[3] = 11
list_2[2].append(12)
print(list_2)	# output => [1, 2, [3, 5, 12], 11]
print(list_1)	# output => [1, 2, [3, 5, 12], 4]

# deep
list_3 = deepcopy(list_1)
list_3[3] = 10
list_3[2].append(13)

print(list_3)	# output => [1, 2, [3, 5, 6, 13], 10]
print(list_1)	# output => [1, 2, [3, 5, 6], 4]