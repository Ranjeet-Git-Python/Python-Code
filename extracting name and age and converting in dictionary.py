import re
messages = '''
jeska is 66 and jems is 34
zac is 45 and mac is 23
'''
pattern = r'(\w+)\s+is\s+(\d+)'
match = re.findall(pattern,messages)
print(match)
print({item[0]:item[1]for item in match})