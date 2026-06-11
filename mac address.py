import re
string = "device Mac 3d:3c:fd:fe:1a:2b and 00-1A-2B-3C-4D-5E"
pattern = r'(?:[0-9a-fA-F]{2}[:-]?){6}'
match = re.findall(pattern,string)
print(match)

import re
log = """
Device 1 (Router): 00.1A.2B.3C.4D.5E connected.
Device 2 (Switch): 1A-2B-3C-4D-5E-6F connected.
Device 3 (Laptop): AA:BB:CC:DD:EE:FF connected.
"""
pattern = r'(?:[0-9a-fA-F]{2}[.:-]?){6}'
match = re.findall(pattern,log)
print(match)
