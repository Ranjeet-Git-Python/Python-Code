def myfunction(fun):
    print("before function ")
    fun()
    print("after function")

@myfunction
def fun1():
    print("hello")
    
fun1