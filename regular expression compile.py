st ="Hi Hello world Hello"

pattern = "He"

import re
print(re.findall(pattern,st))
print(re.search(pattern,st).group(0))
print(re.match("Hi",st).group(0))
print(re.search(r'He\w+', st).group())
print(re.sub("He", "Hi", st))

pattern = re.compile(r'He\w+')
print(pattern.search(st).group())
print(pattern.findall(st))
pattern = re.compile(r'Hi')
print(pattern.match(st).group())