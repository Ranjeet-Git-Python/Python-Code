import re
st ="Hi Hello world Hello"
 
pattern = "He"

print(f"Findall:", re.findall(pattern,st))
print(f"result2:", re.search(pattern,st))
print(f"result2.group(0):", re.search(pattern,st).group(0))
print(f"result2.groups(1):", re.search(pattern,st).groups(1))
print(f"result3:", re.match(pattern,st))
#print(result3.group(0))
#print(result3.groups(1))
print(f"result4:", re.sub('hello','hi', st))
print(f"result5:", re.sub('Hello','hi', st))
print(f"result2:", re.search(r'He\w+', st).group(0))