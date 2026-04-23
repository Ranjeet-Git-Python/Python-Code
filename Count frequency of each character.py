x = "Automation Testing"
p = [char for char in x if char != " "]
q = set(p)
r = list(q)
dict1 = {}
count = 0
for i in r:
    y= x.count(i)
    dict1[i] = y
print(dict1)
dict2 = {}
for key,value in dict1.items():
    if value != 1:
        dict2[key] = value
print(dict2)

#2nd way

x = "Automation Testing"
p = [char for char in x if char != " "]
q = set(p)
r = list(q)
dict1 = {}
count = 0
for i in r:
    y= x.count(i)
    if y != 1:
        dict1[i] = y
print(dict1)

#3rd Method

string1 = "Automation Testing"
chardict = {}
count = 0
for char in string1:
    keys = chardict.keys()
    if char in keys:
        chardict[char] += 1
    else:
        chardict[char] = 1
print(chardict)
q = {x:y for x,y in chardict.items() if y!=1}
print(q)