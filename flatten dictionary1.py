data = {"a": 1, "b": [2, 3, {"c": 4}], "d": {"e": 5, "f": [6, {"g": 7}]}}

def flatten(obj):
    result = []
    if isinstance(obj, dict):
        for v in obj.values():
            result.extend(flatten(v))
    elif isinstance(obj, list):
        for item in obj:
            result.extend(flatten(item))
    else:
        result.append(obj)
    return result

print(flatten(data))  # [1, 2, 3, 4, 5, 6, 7]

def flatten(obj):
    if isinstance(obj,dict):
        items = obj.values()
    elif isinstance(obj,list):
        items = obj
    else:
        return [obj]
    result = []
    for item in items:
        result.extend(flatten(item))
    return result

print(flatten(data))

def flatten(obj):
    if type(obj) == dict:
        items = obj.values()
    elif type(obj)==list:
        items = obj
    else:
        return [obj]
    result = []
    for item in items:
        result.extend(flatten(item))
    return result

print(flatten(data))