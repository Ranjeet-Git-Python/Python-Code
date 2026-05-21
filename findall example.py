import re

target_string = "Emma is a basketball player who was born on June 17, 1993. She played 112 matches with scoring average 26.12 points per game. Her weight is 51 kg."
result = re.findall(r"\d+", target_string)
# print all matches
print("Found following matches")
print(result)
# Output ['17', '1993', '112', '26', '12', '51']

import re

target_string = "Emma is a basketball player who was born on June 17, 1993. She played 112 matches with a scoring average of 26.12 points per game. Her weight is 51 kg."
# finditer() with regex pattern and target string
# \d{2} to match two consecutive digits 
result = re.finditer(r"\d{4}", target_string)

# print all match object
for match_obj in result:
    # print each re.Match object
    print(match_obj)
    
    # extract each matching number
    print(match_obj.group())

import re
target_string = "Jessa is a Python developer. She also gives Python programming training"
# all word starts with letter 'p'
print(re.findall(r'\b[p]\w+\b', target_string, re.I))
# output ['Python', 'Python', 'programming']

# all word starts with substring 'Py'
print(re.findall(r'\bpy\w+\b', target_string, re.I))
# output ['Python', 'Python']

import re

print("2nd program")
target_string = "Jessa is a Python developer. She also gives Python programming training"
# all word starts with letter 'p' and ends with letter 'g'
print(re.findall(r'\b[p]\w+[g]\b', target_string, re.I))
# output 'programming'

# all word starts with letter 'p' or 't' and ends with letter 'g'
print(re.findall(r'\b[pt]\w+[g]\b', target_string, re.I))
# output ['programming', 'training']

target_string = "Jessa loves mango and orange"
# all word starts with substring 'ma' and ends with substring 'go'
print(re.findall(r'\bma\w+go\b', target_string, re.I))
# output 'mango'

target_string = "Kelly loves banana and apple"
# all word starts or ends with letter 'a'
print(re.findall(r'\b[a]\w+\b|\w+[a]\b', target_string, re.I))
# output ['banana', 'and', 'apple']

import re

print("3rd program")
target_string = "Jessa is a knows testing and machine learning"
# find all word that contain letter 'i'
print(re.findall(r'\b\w*[i]\w*\b', target_string, re.I))
# found ['is', 'testing', 'machine', 'learning']

# find all word which contain substring 'ing'
print(re.findall(r'\b\w*ing\w*\b', target_string, re.I))
# found ['testing', 'learning']

import re

str1 = "Emma is a baseball player who was born on June 17, 1993."

# search() for eight-letter word surrounded by space
# \b is used to specify word boundary
result = re.findall(r"\bEmma\b|\bplayer\b|\bborn\b", str1)
print(result)
# Output ['Emma', 'player', 'born']