# counting each word through for loop
text = "the cat sat on the mat the cat"
#Output: {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}
words = text.split(" ")
output = {}
for word in words:
    if word in output:
        output[word]+= 1
    else:
        output[word] = 1
print(output)

# counting each word through get()
output1 = {}
for word in words:
    output1[word] = output1.get(word,0) + 1
print(output1)