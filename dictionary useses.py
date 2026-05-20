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
    product.pop(key,None)
print(product)

user = {"id": 42, "username": "jdoe", "email": "jdoe@example.com", "password": "s3cr3t", "joined": "2021-03-15"} 
keys = ["id", "username", "email"]

#Expected Output: {'id': 42, 'username': 'jdoe', 'email': 'jdoe@example.com'}
dict1 = {}
for key in keys:
    dict1[key]=user.get(key)
print(dict1)

print({item:user[item] for item in user if item in keys})

attributes = ["brand", "model", "year", "color"]
details = ["Honda", "Civic", 2023, "silver"]

#Expected Output: {'brand': 'Honda', 'model': 'Civic', 'year': 2023, 'color': 'silver'}
dict1 = {}
for i,j in zip(attributes,details):
    dict1[i]=j
print(dict1)

print(dict(zip(attributes,details)))

text = "hello world"
text1=text.replace(" ","")
dict1 = {}
for char in text1:
    dict1[char]=dict1.get(char,0)+1
print(dict1)
dict1 = {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
print(sorted(dict1.items(), key = lambda x:x[1]))

scores = {"Alice": 82, "Bob": 45, "Carol": 91, "Dave": 58, "Eve": 73}
#{'Alice': 82, 'Carol': 91, 'Eve': 73}
print({key:value for key,value in scores.items() if value>60})

stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}
min_value=min(stock.values())
print({key for key,value in stock.items() if value==min_value})
print(min(stock,key=stock.get))
print(min(stock.items(),key=lambda x:x[1]))
scores = {"Alice": 88, "Bob": 95, "Carol": 72, "Dave": 95, "Eve": 84}

#Expected Output: Top scorer: Bob
maxmium = max(scores,key=scores.get)
print(maxmium)
print(max(scores.items(),key=lambda x:x[1]))
max_value = max(scores.values())
print({key for key,value in scores.items() if value==max_value})

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