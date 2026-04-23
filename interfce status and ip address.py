import re
message = '''   
        interface    ip    status
    1   eth0       192.168.1.1   up
    2   eth1       192.168.1.2  down
    3   eth2       192.168.1.3  up
    
     '''
#1st way
lines = message.strip().splitlines()
x = lines[0].split()
dict1 = {}
for line in lines[1:]:
    y = line.split()
    dict1.update({y[0]:{x[0]:y[1],x[1]:y[2],x[2]:y[3]}})
print(dict1)

#2nd way
#pattern = r'(\d+)\s+(eth\d)\s+([0-9.]+)\s*(up|down)'
pattern = r'(\d+)\s+(eth\d)\s+([0-9.]+)\s+(\w+)'
result = re.findall(pattern,message)
#print(dict(result))
print(result)
dict2 = {}
for i in result:
    dict2.update({i[0]:{x[0]:i[1],x[1]:i[2],x[2]:i[3]}})
print(dict2)
