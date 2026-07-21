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
