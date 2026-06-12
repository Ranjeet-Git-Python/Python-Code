import re
string = '''FastEthernet0/0 is ely down, line protocol is ab09:5640:fd45 down
 Hardware is DEC21140,address is ca01.3cd1.0000'''
pattern = r'(?:[a-fA-F0-9]{4}[.:]){2}[a-fA-F0-9]{4}'
pattern1 = r'(?:[a-fA-F0-9.:]{5}){2}[a-fA-F0-9]{4}'
match = re.findall(pattern,string)
print(match)
match1 = re.findall(pattern1,string)
print(match1)