#Question 4. Create a dictionary with numbers between 1 and n as keys and their squares as values.
dict1 = {}
for i in range(num1,num2+1):
    dict1.update({i:i*i})
print(dict1)