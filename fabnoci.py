def fibonacci(n):
    a, b = 0, 1
    list1 = []
    for i in range(n):
        a, b = b, a + b
        list1.append(a)
    return list1

print(fibonacci(5))