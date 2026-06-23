nums = [1, 2, 3, 2, 4, 5, 1]
dup = []
uni = []
for i in nums:
    if i in uni:
        dup.append(i)
    else:
        uni.append(i)
print(dup)

#2nd method
duplicates = list(set(x for x in nums if nums.count(x) > 1))

print(duplicates)