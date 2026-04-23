import re
messages = '''
jeska is 66 and jems is 34
zac is 45 and mac is 23
'''
def name_and_age(text):
    pattern = r'(\w+) is (\d+)'
    all_matches = re.findall(pattern,text)
    print(all_matches)
    return {name:int(age) for name,age in all_matches}
    
output = name_and_age(messages)

print(output)