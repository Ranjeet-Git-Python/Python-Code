str1 = "Welcome to USA. usa awesome, isn't it?"
str2 = str1.lower().count("usa")
print(str2)

#vowel count
vowels = "aeiou"
str1 = "Hello World"
vowel_count = 0
for i in str1.lower():
    if i in vowels:
        vowel_count += 1
print("Number of vowels:", vowel_count)

#check prefix/suffix
str1 = "https://google.com"
if str1.startswith("https://"):
    print("The string starts with 'https://'")
if str1.endswith(".com"):
    print("The string ends with '.com'")

#Case Transformation
str1 = "PyThOn"  #output = pYtHoN
str2 = ""
for i in str1:
    if i.isupper():
        str2 += i.lower()
    else:
        str2 += i.upper()
print(str2)

#2nd method
res = str1.swapcase()

print("Original:", str1)
print("Swapped :", res)

