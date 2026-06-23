nums = [3,2,5, "a"]
sum = 0 
for i in nums:
    try:
        sum += i
    except TypeError:
        print("Type error")
    finally:
        print("sum", sum)
        
print("----------------------")
nums = [1,2,5, "a"]
div = 0
for i in nums:
    try:
        div =  i//(i-1)
    except ZeroDivisionError:
        print("we can not devide any number by zero")
    except TypeError:
        print("Can not do division with string")
    finally:
        print("Division result", div)