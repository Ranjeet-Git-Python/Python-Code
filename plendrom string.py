text = "abcdefedcba"
if text == text[::-1]:
    print("palindrom")
else:
    print("no plandirom")

text = "cat a tac"
rev_txt = ""
for char in text:
    rev_txt = char + rev_txt
print(rev_txt)
if text == rev_txt:
    print("palindrom")
else:
    print("no plandirom")

