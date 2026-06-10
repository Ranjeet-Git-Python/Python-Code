string1 = "Automation Testing"
str1 = [char.lower() for char in string1 if char != " "]
count = 0
dict1 = {}
for char in str1:
    if char != " ":
         dict1[char] = str1.count(char)
print(dict1)
#ascending order
print("ascending order:",dict(sorted(dict1.items(), key = lambda x:x[1])))

#2nd way
string1 = "Automation Testing"
count = 0
dict1 = {}
for char in string1:
    if char.lower() in dict1:
        dict1[char.lower()] += 1
    else:
        dict1[char.lower()] = 1
        
print(dict1)
print(dict({item for item in dict1.items() if item[1] != 1}))