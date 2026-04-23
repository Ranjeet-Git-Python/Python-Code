i=0 
list1 = []
counter = 0
while i<64:
    j=0
    while j<256:
        ip = f"192.168.{i}.{j}"
        if j == 0 or j == 255:
            j+=1
            continue
        list1.append(ip)
        print(ip)
        counter += 1
        j+=1
    i+=1

print(f"Total IPs generated: {counter}")
#print(f"Total IPs in list: {len(list1)}")
list1.pop(0)
list1.pop(-1)
print(f"Total IPs in list: {len(list1)}")
#print(list1)

