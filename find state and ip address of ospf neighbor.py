log = '''Neighbor ID     Pri   State           Dead Time   Address         Interface
2.2.2.2           1   FULL/DR         00:00:31    10.1.12.2       Gi0/0
3.3.3.3           1   FULL/BDR        00:00:38    10.1.13.3       Gi0/1
4.4.4.4           1   2WAY/DROTHER    00:00:34    10.1.14.4       Gi0/2'''
import re
pattern = r'\S+\s+\d+\s+(\S+)\s+\S+\s+((?:\d+\.){3}\d+)'
match = re.findall(pattern,log)
print(match)