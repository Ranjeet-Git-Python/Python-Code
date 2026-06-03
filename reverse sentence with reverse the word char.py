text = "the cat sat on the mat the cat"
w1 = ""
w2 = " "
t1 = text.split(" ")
for char in t1:
    for j in char:
        w1 = j + w1
    w2 = w1 +" "+ w2
    w1 = ""
print(w2)