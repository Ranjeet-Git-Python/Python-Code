data = {"a": 1, "b": [2, 3, {"c": 4}], "d": {"e": 5, "f": [6, {"g": 7}]}}

#data = {"a": 1, "b": [2, 3, {"c": 4}], "d": {"e": 5, "f": [6, {"g": 7}]}}
#data = (2,5,7,9,80)
#data = {1,2,4,5,7,9,10,23}
def flatten(obj):
        if isinstance(obj,dict):
            items = obj.values()
        elif isinstance(obj,list):
            items = obj
        elif isinstance(obj,tuple):
            items = obj
        elif isinstance(obj,set):
            items = obj
        else:
            return [obj]
        list1 = []
        for item in items:
           list1.extend(flatten(item))
        return list1

print(flatten(data))

import re
 
data = {"a": 1, "b": [2, 3, {"c": 4}], "d": {"e": 5, "f": [6, {"g": 7}]}}
 
text = str(data)
 
numbers = re.findall(r"\d+", text)
 
# Convert to integers
output = list(map(int, numbers))
 
print(output)


