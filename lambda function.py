a = 'GeeksforGeeks'
upper = lambda x: x.upper()
print(upper(a))

check = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(check(-3))
print(check(0))

func = [lambda arg=x: arg * 10 for x in range(1, 5)]
print(func)
for i in func:
    print(i())

calc = lambda x, y: (x + y, x * y)
res = calc(3, 4)
print(res)

c = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, c)
print(even)
print(list(even))

a = [1, 2, 3, 4]
double = map(lambda x: x * 2, a)
print(double)
print(list(double))

from functools import reduce
a = [1, 2, 3, 4]
mul = reduce(lambda x, y: x * y, a)
print(mul)