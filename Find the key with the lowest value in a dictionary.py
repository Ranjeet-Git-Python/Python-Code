#Question 12. Find the key with the lowest value in a dictionary.

stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}

dict1 = {i for i,j in stock.items() if  j==min(stock.values())}
print(dict1)

#2nd way
stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 18, "mangoes": 23}
'''Use min(dict, key=dict.get) — this passes each key through dict.get to
 retrieve its value for comparison, returning the key whose value is the smallest.
Alternatively, use min(dict.items(), key=lambda item: item[1]) to get the full (key, value)
 tuple for the minimum entry.'''
lowest = min(stock, key=stock.get)
print(lowest)