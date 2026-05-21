import re

multi_line_string = """emma 
love Python"""

# Matches at the start
print(re.match('emma', multi_line_string).group())
# Output 'emma'

# re.match doesn't match at the start of each newline
# It only match at the start of the string
# Won't match
print(re.match('love', multi_line_string, re.MULTILINE))
# Output None

# found "love" at start of newline
print(re.search('love', multi_line_string).group())
# Output 'love'

pattern = re.compile('Python$', re.MULTILINE)
# No Match
print(pattern.match(multi_line_string))
# Output None

# found 'Python" at the end
print(pattern.search(multi_line_string).group())
# Output 'Python'
