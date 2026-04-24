def longest_common_prefix(strs):
    if not strs:
        return ""
        
    shortest = min(strs, key=len)
    print("Shortest string:", shortest)
    for i, char in enumerate(shortest):
        for other in strs:
            if other[i] != char:
                return shortest[:i]
                
    return shortest

# Example usage
strs = ["flower","flow","flight"]
print(longest_common_prefix(strs))

#2nd method
def longest_common_prefix(strs):
    if not strs:
        return ""
        
    prefix = strs[0]
    print("Initial prefix:", prefix)
    
    for s in strs[1:]:
        print("Comparing with:", s)
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            print("Updated prefix:", prefix)
            if not prefix:
                return ""
                
    return prefix


# Example usage
strs = ["flower","flow","flight"]
print(longest_common_prefix(strs))

#3rd method
strs = ["flower","flow","flight"]
prefix = strs[0]
i = 0
for s in strs[1:]:
    if s[i] != prefix[i]:
        prefix = prefix[:i]
        print(prefix)
        break
    i+=1

