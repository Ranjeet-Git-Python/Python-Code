str1 = " P y t h o n "   #Expected Output: Python
str2 = ""
for i in str1:
    if i is not " ":
        str2 += i
print(str2)

#2nd method
str1 = " P y t h o n "

# Replace space with nothing
res = str1.replace(" ", "")

print("Cleaned string:", res)

#N-th Character Removal
str1 = "Python"
i = 2
print(str1[:i]+str1[i+1:])

#String Partitioning
str1 = "username@company.com" #('username', '@', 'company.com')
sep = "@"
par1 = str1.partition("@")
print(par1)


par1 = str1.split("@")
print(par1)

#Extract File Extension
file_name = "report_final_v2.pdf" #output = pdf
ext1 = file_name.split(".")
print(ext1[-1])

#Lowercase First
str1 = "PyNaTive"
str2 = ""
for i in str1:
    if i.islower():
        str2 += i

for i in str1:
        if i.isupper():
            str2 += i
print(str2)

#2nd method
str1 = "PyNaTive"
lower = []
upper = []

for char in str1:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)

# Join both lists
print(lower + upper)
res = "".join(lower + upper)
print("Result:", res)

#Count all letters, digits, and special symbols from a given string
str1 = "P@#yn26at^&i5ve" # output = Total counts of chars, digits, and symbols: Chars = 8 Digits = 3 Symbol = 4
char_count = 0
digt_count = 0
spl_char_count = 0
for i in str1:
    if i.isalpha():
        char_count += 1
    elif i.isdigit():
        digt_count += 1
    else:
        spl_char_count += 1
print(f"Total counts of chars, digits, and symbols: Chars = {char_count} Digits = {digt_count} Symbol = {spl_char_count}")

#Create a mixed string using alternating characters
s1 = "Abc" 
s2 = "Xyz"
mixed_string = ""
for i in range(0, max(len(s1), len(s2))):
        mixed_string += s1[i]
        mixed_string += s2[-(i+1)]
print(mixed_string)

#string with different length
s1 = "Abc" 
s2 = "Xyzo"
mixed_string = ""
for i in range(0, max(len(s1), len(s2))):
        if i < len(s1):
            mixed_string += s1[i]
        if i < len(s2):
            mixed_string += s2[-(i+1)]
print(mixed_string)

#Calculate the sum and average of the digits present in a string
str1 = "PYnative29@#8496"  #Output: Sum is: 38 Average is 6.33
sum1 = 0
count = 0
for i in str1:
     if i.isdigit():
        sum1 += int(i)
        count += 1
print(f"Sum is: {sum1}")
print(f"Average is: {sum1/count:.2f}")

#Count occurrences of all characters within a string
str1 = "apple"  #Output: {'a': 1, 'p': 2, 'l': 1, 'e': 1}
char_count = {}
for i in str1:
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1
print(f"Output: {char_count}")
