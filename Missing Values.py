
t1 = [11, 12, 14, 15, 19]

missing = [x for x in range(min(t1), max(t1) + 1) if x not in t1]
print(missing)
t1.extend(missing)
t1.sort()

print(t1)
