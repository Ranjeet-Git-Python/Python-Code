def mydec(func):
    def wrapper():
        print ("This is first")
        func()
        print ("This is second")
    return wrapper
@mydec
def hello():
    print ("Hello")
@mydec
def hellox():
    print ("Hello1")
hello()
hellox()