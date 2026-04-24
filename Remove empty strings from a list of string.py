str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# Method 1: Using list comprehension
output = [s for s in str_list if s]
print("Output:", output)

# Method 2: Using filter() function
output = list(filter(None, str_list))
print("Output:", output)

# Method 3: Using a for loop
output = []
for s in str_list:
    if s:
        output.append(s)
print("Output:", output)

# Method 4: Using lambda function with filter()
output = list(filter(lambda s: s, str_list))
print("Output:", output)

# Method 5: Using a while loop
output = []
i = 0
while i < len(str_list):
    if str_list[i]:
        output.append(str_list[i])
    i += 1
print("Output:", output)

# Method 6: Using the built-in filter() function with a custom function
def is_not_empty(s):
    return s != "" and s is not None
output = list(filter(is_not_empty, str_list))
print("Output:", output)

# Method 7: Using the built-in filter() function with a lambda function
output = list(filter(lambda s: s != "" and s is not None, str_list))
print("Output:", output)

# Method 8: Using the built-in filter() function with a generator expression
output = list(filter(lambda s: s != "" and s is not None, (s for s in str_list)))
print("Output:", output)
