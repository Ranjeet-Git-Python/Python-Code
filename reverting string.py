

text = "the cat sat on the mat the cat"
print(text)
#Reverting sentence : cat the mat the on sat cat the
l3 = []
l2 = text.split(" ")
for i in range(len(text.split(" "))):
    str1 = ""
    str1 += l2[-i-1]
    l3.append(str1)

print("Reverting sentence :", " ".join(l3))

#Reverting each word : eht tac tas no eht tam eht tac
l1 = []
for i in text.split(" "):
    str1 = ""
    for j in range(len(i)):
        str1 += i[-j-1]
    l1.append(str1)
print("Reverting each word :"," ".join(l1))

#Reverting sentance and each word : tca eth tma eth no tsa tca eth
l3 = []
l2 = text.split(" ")
for i in range(len(text.split(" "))):
    str1 = ""
    str1 += l2[-i-1]
    str2 = ""
    for j in range(len(str1)):
        str2 += str1[j-1]
    l3.append(str2)

print("Reverting sentance and each word :", " ".join(l3))