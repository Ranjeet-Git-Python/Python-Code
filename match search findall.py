import re

target_string = "Jessa loves Python and pandas"
# Match six-letter word
pattern = r"\w{6}"

# match() method
result = re.match(pattern, target_string)
print(result)
# Output None

# search() method
result = re.search(pattern, target_string)
print(result.group()) 
# Output 'Python'

# findall() method
result = re.findall(pattern, target_string)
print(result) 
# Output ['Python', 'pandas'] 


import re

str1 = "Emma 12 25"
# Match any character
print(re.match(r'.', str1))
# output 'E'

# Match all digits
print(re.findall(r'\d', str1))
# Output ['1', '2', '2', '5']

# Match all numbers
# + indicate 1 or more occurence of \d
print(re.findall(r'\d+', str1))
# output ['12', '25']

# Match all special characters and symbols
str2 = "Hello #Jessa!@#$%"
print(re.findall(r'\W', str2))
# Output [' ', '#', '!', '@', '#', '$', '%']