data = {"a": 1, "b": [2, 3, {"c": 4}], "d": {"e": 5, "f": [6, {"g": 7}]}}
str1 = str(data)
import re
match = re.findall(r'\d+',str1)
print(", ".join(match))
print(list(map(int,match)))