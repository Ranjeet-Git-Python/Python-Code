str1 = "/*Jon is @developer & musician!!" #Output: "Jon is developer musician"
# Method 1: Using regular expressions
import re
clean_str = re.sub(r'[^\w\s]', '', str1)
print("Cleaned string:", clean_str)

# Method 2: Using string translation

# method 3: Using a for loop and string concatenation
clean_str = ""
for char in str1:
    if char.isalnum() or char.isspace():
        clean_str += char
print("Cleaned string:", clean_str)