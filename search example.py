import re

# Target String
target = "Emma is a baseball player who was born on June 17"

# search() for eight-letter word
result = re.search(r"\w{8}", target)

# Print match object
print("Match Object", result)
# output re.Match object; span=(10, 18), match='baseball'

# print the matching word using group() method
print("Matching word: ", result.group()) 
# Output 'baseball'

import re

# Target String
target_string = "Emma is a baseball player who was born on June 17, 1993."

# find substring 'ball'
result = re.search(r"ball", target_string)

# Print matching substring
print(result.group())
# output 'ball'

# find exact word/substring surrounded by word boundary
result = re.search(r"\bball\b", target_string)
if result:
    print(result)
# output None

# find word 'player'
result = re.search(r"\bplayer\b", target_string)
print(result.group())
# output 'player'

import re

target_string = "Emma is a basketball player who was born on June 17."

# two group enclosed in separate ( and ) bracket
result = re.search(r"(\w{10}).+(\d{2})", target_string)

# Extract the matches using group()

# print ten-letter word
print(result.group(1))
# Output basketball

# print two digit number
print(result.group(2))
# Output 17

import re

# Target String
target_string = "Emma is a Baseball player who was born on June 17, 1993."

# case sensitive searching
result = re.search(r"emma", target_string)
print("Matching word:", result)
# Output None

print("case insensitive searching")
# using re.IGNORECASE
result = re.search(r"emma", target_string, re.IGNORECASE)
print("Matching word:", result.group())
# Output 'Emma'

target_string = "Emma is a Baseball player who was born on June 17, 1993."
import re

print(re.search(r'emma', target_string, re.I).group())