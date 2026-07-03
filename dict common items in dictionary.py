d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"a": 1, "b": 99, "c": 3}
#Expected Output: Intersection: {'a': 1, 'c': 3}
print(dict({item for item in d1.items() if item in d2.items()}))

print({key:value for key,value in d1.items() if d1[key]==d2[key]})