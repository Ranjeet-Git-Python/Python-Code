import re
st ="Hi Hello world Hello"
 
pattern = "He"
 
result1 = re.findall(pattern,st)
result2 = re.search(pattern,st)
result3 = re.match(pattern,st)
result4 = re.sub('hello','hi', st)
result5 = re.sub('Hello','hi', st)
print(result1)
print(result2)
print(result2.group(0))
print(result2.groups(1))
print(result3)
#print(result3.group(0))
#print(result3.groups(1))
print(result4)
print(result5)