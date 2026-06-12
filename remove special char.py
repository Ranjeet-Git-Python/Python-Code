str1 = "/*Jon is @developer & musician!!"
str2 = ""
for char in str1:
    if char.isalpha() or char.isspace():
        str2 += char
print(str2)

import re
str3 = re.sub("[^\w\s]", "",str1)
print(str3)