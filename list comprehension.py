'''Practice Problem: Write a single-line list comprehension that takes a list of strings, filters out strings shorter than 4 characters, and converts the remaining strings to uppercase'''

words = ["apple", "bat", "cherry", "dog", "elderberry"]
#Output: ['APPLE', 'CHERRY', 'ELDERBERRY']
l1 = [i.upper() for i in words if len(i)>4]
print(l1)
'''Write a function that merges two dictionaries. If a key exists in both dictionaries, sum their values. If a key exists in only one, include it as is.'''

dict_a = {'a': 10, 'b': 20} 
dict_b = {'b': 5, 'c': 15}
# Output: Merged Dictionary: {'a': 10, 'b': 25, 'c': 15}
# d1 = {i:j for i,j in dict_a.items() if i in dict_b}
# print(d1)
d1 = {}
for i in dict_a.keys():
    for j in dict_b.keys():
        if i == j:
            d1[i]= dict_a[i]+dict_b[j]
        else:
            d1[i]=dict_a[i]
            d1[j]=dict_b[j]
print(d1)

#2nd way
d1 = {'a': 10, 'b': 20} 
d2 = {'b': 5, 'c': 15}
d3 = d1.copy()
for i, j in d2.items():
    d3[i]=d3.get(i,0)+j
print(d3)

'''Create a function that takes a string and returns a count of how many times each character appears. Ignore spaces and make it case-insensitive.'''
text = "Python Programming"
l1 =[i.lower() for i in text if i !=" "]
d1 = {}
for i in l1:
    if i in d1:
        d1[i] += 1
    else:
        d1[i] = 1
print(d1)
 
 #2nd way
from collections import Counter
t1=text.replace(" ", "")
print(Counter(t1.lower()))
    
word1 = "listen"
word2 = "silent"

def augmented(word1,word2):
    count=0
    if len(word1)==len(word2):
        for i in word1:
            if i in word2:
                count+=1
            else:
                print("not agumented word")
        return count
    else:
        print("Both are not agumented word")
        
if augmented(word1,word2) == len(word1):
    print("Both are agumented word" )
#2nd way
def is_anagram(str1, str2):
    # Clean and sort both strings
    s1 = sorted(str1.lower().replace(" ", ""))
    s2 = sorted(str2.lower().replace(" ", ""))
    # If the sorted lists are identical, they are anagrams
    return s1 == s2

w1, w2 = "listen", "silent"
result = is_anagram(w1, w2)
print(f'Is "{w1}" an anagram of "{w2}"? {result}')


nested = [1, [2, 3], [4, [5, 6]], 7]
#Flattened: [1, 2, 3, 4, 5, 6, 7]
l1 = []
def flatten(nested):
    for i in nested:
        if isinstance(i, list):
            flatten(i)
        else:
            l1.append(i)
    return l1
print(flatten(nested))

#2nd way
def flatten(lst):
    flat_list = []
    
    for item in lst:
        if isinstance(item, list):
            # Recursion: if it's a list, flatten it and extend our results
            flat_list.extend(flatten(item))
        else:
            # Base case: it's a single value, just add it
            flat_list.append(item)
            
    return flat_list

nested_data = [1, [2, 3], [4, [5, 6]], 7]
result = flatten(nested_data)

print(f"Original:  {nested_data}")
print(f"Flattened: {result}")
#palindrome
s1= "A man, a plan, a canal: Panama"
#Output: True
l1 =[char.lower() for char in s1 if char.isalnum()]
print("sentence is palindrome:", l1 == l1[::-1])
#2nd way
def is_palindrome_sentence(sentence):
    # Filter out punctuation and spaces, convert to lowercase
    clean_chars = [char.lower() for char in sentence if char.isalnum()]
    
    # Join into a string
    clean_str = "".join(clean_chars)
    
    # Compare with its reverse
    return clean_str == clean_str[::-1]

# Usage
test_s = "A man, a plan, a canal: Panama"
print(f"Is palindrome? {is_palindrome_sentence(test_s)}")

'''Given a list of strings, use a single list comprehension to extract strings that meet two criteria: they must be longer than 5 characters AND they must start with a vowel (a, e, i, o, u).'''

l1=["apple", "education", "ice", "ocean", "python", "umbrella"]
# Output: ['education', 'umbrella']
l2 = []
vowels = ["a","e","i","o","u"]
for i in l1:
    if len(i)>5 and i[0].lower() in vowels:
        l2.append(i)
print(l2)
#2nd way
l2 = []
#vowels = ["a","e","i","o","u"]
for i in l1:
    if len(i)>5 and i[0].lower() in "aeiou":
        l2.append(i)
print(l2)
'''Write a function that removes duplicate elements from a list. You cannot use set() because sets do not maintain the original order of elements.
'''
l1=[1, 2, 2, 3, 1, 4, 2]
# Output: [1, 2, 3, 4]
l2 =[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)

'''Create a function rotate_list(lst, n, direction) that shifts the elements of a list by N positions. The direction can be ‘left’ or ‘right’.'''
List= [1, 2, 3, 4, 5] 
shift= 2 
Direction= 'right'
l2=List.copy()
#Output: [4, 5, 1, 2, 3]
dir1 = input("Enter direction:")
if dir1 == "right":
    for j in range(shift):
        l2.insert(0,l2.pop())
        #print(l2)
elif dir1 == "left":
    for j in range(shift):
        l2.append(l2.pop(0))
        #print(l2)
else:
    print("print asit is:", List)

print(l2)