#Question: Write a Python program to split a string into a list of substrings based on a specified delimiter (e.g., hyphen) and print each substring on a new line.
str1 = "Emma-is-a-data-scientist"
str2 = str1.split("-")
print(str2)
for i in str2:
    print(i)