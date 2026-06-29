#1st occurance of non-repeating character in a string
str1 = "aaabbcdef"
for char in str1:
    if str1.count(char) == 1:
        print(char)
        break