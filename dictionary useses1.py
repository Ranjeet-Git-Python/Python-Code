keys = ["math", "science", "english", "history"] 
default = 0
output = dict.fromkeys(keys,default)
print(output)

employee = {"fname": "John", "age": 30, "dept": "Engineering"} 
#— rename "fname" to "first_name"
employee["first_name"] = employee.pop("fname")
print(employee)

product = {"id": 101, "name": "Laptop", "price": 999, "stock": 50, "warehouse": "A3"}
remove_keys = ["stock", "warehouse"]
for key in remove_keys:
    product.pop(key)
    #product.pop(key, None)
print(product)