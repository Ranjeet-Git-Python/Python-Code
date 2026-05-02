#Q: What is a decorator in Python and how does it work? Provide an example.A decorator in Python is a design pattern that allows you to modify the behavior of a function or class
def mydec(func):
    def wrapper():
        print ("This is first")
        func()
        print ("This is second")
    return wrapper
@mydec
def hello():
    print ("Hello")
    print ("Hi")
@mydec
def hellox():
    print ("Hello1")

hello()
hellox()