import re

string = '''Neighbor ID Pri State Dead Time Address Interface
•192.168.1.5 1 FULL/DR 00:00:32 10.0.0.2 GigabitEthernet1
•10.0.0.3 1 FULL/BDR 00:00:35 192.168.10.3 GigabitEthernet2'''

matches = re.findall(r'(\d+\.\d+\.\d+\.\d+)\s+\d+\s+(\S+)', string)

print(matches)