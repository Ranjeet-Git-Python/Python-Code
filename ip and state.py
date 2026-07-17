import re

string = '''Neighbor ID Pri State Dead Time Address Interface
•192.168.1.5 1 FULL/DR 00:00:32 10.0.0.2 GigabitEthernet1
•10.0.0.3 1 FULL/BDR 00:00:35 192.168.10.3 GigabitEthernet2'''
output= string.splitlines()
dict1 = {}
for line in output[1:]:
    #match = re.search(r'(\d+\.\d+\.\d+\.\d+)\s+\d+\s+(\S+)', line)
    match = re.search(r'((\d{1,3}\.){3}\d{1,3})\s+\d+\s+(\S+)', line)
    #Note: because of the nested group (\d{1,3}\.){3}, the state becomes group(3). To avoid that, use a non-capturing group:
    if match:
        ip = match.group(1)
        state = match.group(3)
        dict1[ip] = state
    print("IP:", ip)
    print("State:", state)
print(dict1)