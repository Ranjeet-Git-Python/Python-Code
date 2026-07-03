# short char of sentance
input1 = input("enter the sentence:")
l1= [i for i in input1.split()]
print(l1)
words = input1.split(" ")
print(" ".join(sorted(list(set(words)))))