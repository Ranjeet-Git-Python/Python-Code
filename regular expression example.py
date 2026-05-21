import re
string = "ABCDEFabcdef123450"
pattern = re.compile(r'[^a-zA-Z0-9]')
match = pattern.search(string)
print(match)

def extract_date(url):
        return re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url)
url1= "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
print(extract_date(url1))

# Solution
def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\2-\\3-\\1', dt)
#1. Breakdown of the Pattern: r'(\d{4})-(\d{1,2})-(\d{1,2})'The pattern finds a specific sequence of characters and remembers each part inside parentheses:(\d{4}) (Group 1): Matches exactly 4 digits in a row (the year 2026).-: Matches the literal hyphen character.(\d{1,2}) (Group 2): Matches 1 or 2 digits in a row (the month 01).-: Matches the second literal hyphen character.(\d{1,2}) (Group 3): Matches 1 or 2 digits in a row (the day 02).2. Breakdown of the Replacement: '\\3-\\2-\\1'The re.sub() function replaces the entire matched date with a new format using backreferences to the groups:
#   \\3: Inserts whatever was caught in Group 3 (the day: 02).-: Inserts a hyphen.\\2: Inserts whatever was caught in Group 2 (the month: 01).-: Inserts a hyphen.\\1: Inserts whatever was caught in Group 1 (the year: 2026).This turns "2026-01-02" directly into "02-01-2026".
dt1 = "2026-01-20"
print("Original date in YYY-MM-DD Format: ",dt1)
print("New date in DD-MM-YYYY Format: ",change_date_format(dt1))

# Sample string.
text = "Ten 10, Twenty 20, Thirty 30"
result = re.split("\D+", text)
# Print results. re.split("\D+", text) splits the string at every sequence of non-digits.The non-digit separators "Ten ", ", Twenty ", and ", Thirty " are removed.This leaves only the digit groups as elements in the resulting list.
for element in result:
    print(element)

text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
#find all the words starting with 'a' or 'e'
list = re.findall("[ae]\w+", text)
# Print result.
print(list)

#Q.Write a Python program to separate and print the numbers and their position of a given string
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

for m in re.finditer("\d+", text):
    print(m.group(0))
    print("Index position:", m.start())

#Q.Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.
street = '21 Ramkrishna Road'
print(re.sub('Road$', 'Rd.', street))

text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.findall(pattern, text):
    print('Found "%s"' % match)

pattern = 'fox'
text = 'The quick brown fox jumps over the lazy dog.'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print('Found "%s" in "%s" from %d to %d ' % (match.re.pattern, match.string, s, e))

patterns = [ 'fox', 'dog', 'horse' ]
text = 'The quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    print('Searching for "%s" in "%s" ->' % (pattern, text),)
    if re.search(pattern,  text):
        print('Matched!')
    else:
        print('Not Matched!')

results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12, 13, and 345 are important")
print("Number of length 1 to 3")
for n in results:
     print(n.group(0))