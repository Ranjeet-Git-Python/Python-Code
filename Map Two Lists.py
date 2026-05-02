attributes = ["brand", "model", "year", "color"]
details = ["Honda", "Civic", 2023, "silver"]

# Output: {'brand': 'Honda', 'model': 'Civic', 'year': 2023, 'color': 'silver'}
dict1 = {}
for i, j in zip(attributes, details):
    dict1[i] = j
print(dict1)

#2nd way
dict2 = dict(zip(attributes, details))
print(dict2)