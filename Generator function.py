
'''A generator is a special type of function in Python
that produces values one at a time using yield instead of return.'''
def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num, end=" ")
