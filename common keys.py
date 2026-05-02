d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "c": 30, "d": 40}

common_keys = d1.keys() & d2.keys()

print("Common keys:", common_keys)

#2nd way
common_keys = set(d1.keys()).intersection(d2.keys())
print("Common keys (2nd way):", common_keys)

#3rd way
common_keys = [key for key in d1.keys() if key in d2]
print("Common keys (3rd way):", common_keys)

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
l1 =[]
p= 1
for i in range(num1,num2+1):
    for j in range(1,i+1):
        p=j*p
    l1.append(str(p))
    p=1
str2=",".join(l1)
print(str2)
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
        
p=fact(4)
print(p)
##########
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
l1 =[]
p= 1
for i in range(num1,num2+1):
    p=fact(i)
    l1.append(str(p))
    p=1
str2=",".join(l1)
print(str2)
##############
dict1 = {}
for i in range(num1,num2+1):
    dict1.update({i:i*i})
print(dict1)

num1 = input("Enter the first number")
x=num1.split(",")
print(x)
print(tuple(x))
class abc():
   
    def __init__(self):
        pass
    def getstring(self):
        input1 = input("enter string:")
        self.input1=input1
        
    def printstring(self):
        print("print string:", self.input1.upper())

obj = abc()
obj.getstring()
obj.printstring()
import math
input1 = input("enter string:")
l1=input1.split(",")
l2=[]
c=50
h= 30
for i in l1:
    Q=math.sqrt((2*c*int(i))/h)
    l2.append(str(int(Q)))

print(",".join(l2))
x=3
y=5
l2=[]
for i in range(x):
    l1=[]
    for j in range(y):
        l1.append(i*j)
    l2.append(l1)
print(l2)
######################
str1 = "without,hello,bag,world"
l1=str1.split(",")
l1.sort()
print(",".join(l1))
#str1.split().sort()
#print(str1)
str1= '''Hello world
Practics makes perfect'''
print(str1.capitalize())
print(str1.upper())
print(str1)
l1=str1.split(" ")
l2=[]
for i in l1:
    l2.append(i.upper())
input1 = input("enter the sentence:")
l1= [i for i in input1.split()]
print(l1)
words = input1.split(" ")
print(" ".join(sorted(list(set(words)))))
input1 = input("Enter the binary number:")
l1 = input1.split(",")
l2=[]
for i in l1:
    x = int(i,2)
    if x%5==0:
        l2.append(i)
print(",".join(l2))
dict1={'first':'Bob', 'last':'Smith'}
print(str(dict1))
print(type(str(dict1)))
the_list = [2, 3, 5, 7, 11]

# list comprehension
squared_list = [x**2 for x in the_list]
print(squared_list)
# output is [4 , 9 , 25 , 49 , 121]

# dict comprehension
squared_dict = {x:x**2 for x in the_list}
print(squared_dict)
print(type(squared_dict))
# output is {11: 121, 2: 4 , 3: 9 , 5: 25 , 7: 49}

from copy import copy, deepcopy

list_1 = [1, 2, [3, 5], 4]

# shallow

list_2 = copy(list_1)
list_2[3] = 11
list_2[2].append(12)

print(list_2)	# output => [1, 2, [3, 5, 12], 11]
print(list_1)	# output => [1, 2, [3, 5, 12], 4]

# deep

list_3 = deepcopy(list_1)
list_3[3] = 10
list_3[2].append(13)

print(list_3)	# output => [1, 2, [3, 5, 6, 13], 10]
print(list_1)	# output => [1, 2, [3, 5, 6], 4]

def squares():
  x = range(1, 4) # 1 to 4
  for n in x:
      yield n**2
   
for y in squares():
	print(y)   	# prints 1 4 9 16

data = {"school": {"department": {"class": {"teacher": "Mr. Smith", "students": 30}}}} #— update students to 35

#Output: {'school': {'department': {'class': {'teacher': 'Mr. Smith', 'students': 35}}}}
data["school"]["department"]["class"]["students"]=35
print(data)

squares = {n: n ** 2 for n in range(1, 11)}
print(squares)

scores = {"Alice": 82, "Bob": 45, "Carol": 91, "Dave": 58, "Eve": 73} #— keep only scores greater than 60

#Output: {'Alice': 82, 'Carol': 91, 'Eve': 73}
dict1 = {i:j for i,j in scores.items() if  j>60}
print(dict1)

stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}
#Lowest stock item: grapes
dict1 = {i for i,j in stock.items() if  j==min(stock.values())}
print(dict1)

stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}

lowest = min(stock, key=stock.get)
print("Lowest stock item:", lowest)

pairs = [("name", "Alice"), ("age", 25), ("city", "Paris")]
dict1={i[0]:i[1] for i in pairs}
print(dict1)

pairs = [("name", "Alice"), ("age", 25), ("city", "Paris")]
result = dict(pairs)
print(result)

d1 = {"a": 1, "b": 2, "c": 3} 
d2 = {"b": 20, "c": 30, "d": 40}
dict2={key for key in d1.keys() if key in d2}
print(dict2) # Output: Common keys: {'b', 'c'}

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "d": 40}
#Keys only in d1: {'a', 'c'}
dict2={key for key in d1.keys() if key not in d2}
print(dict2)

only_in_d1 = d1.keys() - d2.keys()

print("Keys only in d1:", only_in_d1)
#intersection of items in two dictionary
d1 = {"a": 1, "b": 2, "c": 3} 
d2 = {"a": 1, "b": 99, "c": 3}
#Output: Intersection: {'a': 1, 'c': 3}
dict2={item for item in d1.items() if item in d2.items()}
print(dict2)
intersection = {k: d1[k] for k in d1.keys() & d2.keys() if d1[k] == d2[k]}
print("Intersection:", intersection)
# counting each word through for loop
text = "the cat sat on the mat the cat"
#Output: {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}
words = text.split(" ")
output = {}
for word in words:
    if word in output:
        output[word]+= 1
    else:
        output[word] = 1
print(output)

# counting each word through get()
output1 = {}
for word in words:
    output1[word] = output1.get(word,0) + 1
print(output1)
# counting each word through counter function
from collections import Counter
word_count = Counter(text.lower().split())
print(word_count)
#remove None contaning items
data = {"name": "Alice", "age": None, "city": "Paris", "score": None}
#Output: {'name': 'Alice', 'city': 'Paris'}
dict1 ={i:j for i,j in data.items() if j!=None}
dict2 ={i:j for i,j in data.items() if None in data.values()}
print(dict1)
print(dict2)
#short by keys
data = {"banana": 3, "apple": 5, "cherry": 1, "date": 4}
dict1 = sorted(data)
dict2 = dict(sorted(data.items(), reverse=True))
print(dict2)
# short by values
scores = {"Alice": 88, "Bob": 72, "Charlie": 95, "Diana": 60}
dict1 = dict(sorted(scores.items(), key=lambda item:item[1]))
print(dict1)

#find unique values in dictionary
data = {"a": 1, "b": 2, "c": 3, "d": 2}
d1 =[]
def unique(data):
    for i in data.values():
        if i in d1:
            return False
            break
        else:
            d1.append(i)

#find unique values in dictionary
d2= unique(data)
if d2 is False:
    print(False)
else:
    print(True)
#2nd Method    
unique = len(data.values()) == len(set(data.values()))
print(unique)

main = {"a": 1, "b": 2, "c": 3, "d": 4} 
subset = {"a": 1, "c": 3}
main_items = main.items()
subset_items = subset.items()
if subset_items <= main_items:
    print(True)

#dictionary to json
import json
person = {"name": "Alice", "age": 30, "address": {"city": "Mumbai", "pin": "400001"}}
print(json.dumps(person,indent=4))

#key to value and value to key
original = {"a": 1, "b": 2, "c": 3}
# Output: {1: "a", 2: "b", 3: "c"}
print({j:i for i,j in original.items()})

#converting key to value and value to key in following way
original = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
# Output: {1: ["a", "c"], 2: ["b", "e"], 3: ["d"]}
inverted = {}
for k, v in original.items():
    inverted.setdefault(v, []).append(k)
print(inverted)

#flaten nested dictionary
nested = {"a": 1, "b": {"c": 2, "d": {"e": 3, "f": 4}}}
#Output: {"a": 1, "b.c": 2, "b.d.e": 3, "b.d.f": 4}
def flatten_dict(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

flattened = flatten_dict(nested)
print(flattened)
