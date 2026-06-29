strs = ["flower","flow","flight"]
prefix = strs[0]
for i in range(len(prefix)):
    for s in strs[1:]:
        if i >= len(s) or s[i] != prefix[i]:
            prefix = prefix[:i]
            print("prefix:", prefix)
            break
    else:
        continue
    break