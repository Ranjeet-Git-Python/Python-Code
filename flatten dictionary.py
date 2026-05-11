data = {"a": 1, "b": [2, 3, {"c": 4}], "d": {"e": 5, "f": [6, {"g": 7}]}}

def flatten_values(obj):
    if isinstance(obj, dict):
        items = obj.values()
    elif isinstance(obj, list):
        items = obj
    else:
        return [obj]
    result = []
    for item in items:
        result.extend(flatten_values(item))
    return result

print(flatten_values(data))