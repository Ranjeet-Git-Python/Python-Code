d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "c": 30, "d": 40}
#Expected Output: Common keys: {'b', 'c'}
print({key for key in d1 if key in d2})
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "d": 40}
#Expected Output: Keys only in d1: {'a', 'c'}
print({key for key in d1 if key not in d2})
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"a": 1, "b": 99, "c": 3}
#Expected Output: Intersection: {'a': 1, 'c': 3}
print({key:value for key,value in d1.items() if d1[key]==d2[key]})