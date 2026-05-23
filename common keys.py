#Question 1: Find common keys in two dictionaries.
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

#question 2: Factorial of a number using recursion and iteration
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
#2nd way
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
        
p=fact(4)
print(p)
#Question 3. factorial of a number using recursion and iteration between two numbers
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
#Question 4. Create a dictionary with numbers between 1 and n as keys and their squares as values.
dict1 = {}
for i in range(num1,num2+1):
    dict1.update({i:i*i})
print(dict1)

num1 = input("Enter the first number")
x=num1.split(",")
print(x)
print(tuple(x))
#Question 5. Map two lists into a dictionary.
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
#Question 6. Square root of a number using math module
import math
input1 = input("enter number as string:")
l1=input1.split(",")
l2=[]
c=50
h= 30
for i in l1:
    Q=math.sqrt((2*c*int(i))/h)
    l2.append(str(int(Q)))

print(",".join(l2))
#Question 7. Create a 2D list (list of lists) with dimensions x and y, where each element is the product of its indices.
x=3
y=5
l2=[]
for i in range(x):
    l1=[]
    for j in range(y):
        l1.append(i*j)
    l2.append(l1)
print(l2)

input1 = input("enter the sentence:")
l1= [i for i in input1.split()]
print(l1)
words = input1.split(" ")
print(" ".join(sorted(list(set(words)))))

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

#Question 9. Update a nested dictionary with a new value for a specific key.
data = {"school": {"department": {"class": {"teacher": "Mr. Smith", "students": 30}}}} #— update students to 35

#Output: {'school': {'department': {'class': {'teacher': 'Mr. Smith', 'students': 35}}}}
data["school"]["department"]["class"]["students"]=35
print(data)
#Question 10. Create a dictionary that maps numbers between 1 and n to their squares using dictionary comprehension.
squares = {n: n ** 2 for n in range(1, 11)}
print(squares)

#Question 11. Filter a dictionary to keep only key-value pairs where the value is greater than a specified threshold.
scores = {"Alice": 82, "Bob": 45, "Carol": 91, "Dave": 58, "Eve": 73} 
#— keep only scores greater than 60
#Output: {'Alice': 82, 'Carol': 91, 'Eve': 73}
dict1 = {i:j for i,j in scores.items() if  j>60}
print(dict1)
#Question 12. Find the key with the lowest value in a dictionary.
stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}
#Lowest stock item: grapes
dict1 = {i for i,j in stock.items() if  j==min(stock.values())}
print(dict1)
#Question 13. Convert a list of key-value pairs into a dictionary.
stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}

lowest = min(stock, key=stock.get)
'''Use min(dict, key=dict.get) — this passes each key through dict.get to retrieve its value for comparison, returning the key whose value is the smallest.
Alternatively, use min(dict.items(), key=lambda item: item[1]) to get the full (key, value) tuple for the minimum entry.'''
print("Lowest stock item:", lowest)
#Question 14. Create a dictionary from a list of tuples, where each tuple contains a key and a value.
pairs = [("name", "Alice"), ("age", 25), ("city", "Paris")]
dict1={i[0]:i[1] for i in pairs}
print(dict1)
#2nd way
pairs = [("name", "Alice"), ("age", 25), ("city", "Paris")]
result = dict(pairs)
print(result)
#Question 15. Find the common keys between two dictionaries and create a new dictionary with those keys and their corresponding values from one of the original dictionaries.
d1 = {"a": 1, "b": 2, "c": 3} 
d2 = {"b": 20, "c": 30, "d": 40}
dict2={key: d1[key] for key in d1.keys() if key in d2}
print(dict2) # Output: Common keys: {'b', 'c'}
#Question 16. Find the intersection of two dictionaries, where the intersection includes only the key-value pairs that are present in both dictionaries with the same value.
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "d": 40}
#Keys only in d1: {'a', 'c'}
dict2={key for key in d1.keys() if key not in d2}
print(dict2)
#2nd way
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
#Question 17. Check if a dictionary is a subset of another dictionary.
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
