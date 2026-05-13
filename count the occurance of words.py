text = "the cat sat on the mat the cat"
#output: {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}
dict1 = {}
for word in text.split(" "):
    dict1[word] = dict1.get(word,0)+1
print(dict1)


dict1 = {}
for word in text.split(" "):
    if word in dict1:
        dict1[word] +=1
    else:
        dict1[word] = 1
print(dict1)