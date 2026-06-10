dict1 = {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
print(sorted(dict1.items(), key = lambda x:x[1]))

dict1 = {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
print("sorted only keys",sorted(dict1, key = lambda x:x[0]))
print("sorted items by key",sorted(dict1.items(), key = lambda x:x[0]))
print("sorted items by values",sorted(dict1.items(), key = lambda x:x[1]))
                