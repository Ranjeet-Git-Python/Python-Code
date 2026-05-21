import re
string = '''FastEthernet0/0 is ely down, line protocol is ab09:5640:fd45 down
 Hardware is DEC21140,address is ca01.3cd1.0000'''
macaddress = re.findall(r'(?:[0-9a-fA-F]{4}[:.]){2}[0-9a-fA-F]{4}', string)
print(macaddress)

string = "device Mac 3d:3c:fd:fe:1a:2b"
m = re.findall(r'\b(?:[0-9a-fA-F]{2}[:-]){5}[0-9a-fA-F]{2}\b', string)
print(m)

#2nd method
string = "device Mac 3d:3c:fd:fe:1a:2b and 00-1A-2B-3C-4D-5E"
m = re.search(r'\b([0-9a-fA-F]{2}[:.-]){5}[0-9a-fA-F]{2}\b', string)
print(m.group(0))

#3rd method
string = "device Mac 3d:3c:fd:fe:1a:2b"
m = re.search(r'\b([0-9a-fA-F]{2}[:.-]){5}[0-9a-fA-F]{2}\b', string)
print(m.group())

import re

# Sample text containing three device MAC addresses
log = """
Device 1 (Router): 00.1A.2B.3C.4D.5E connected.
Device 2 (Switch): 1A-2B-3C-4D-5E-6F connected.
Device 3 (Laptop): AA:BB:CC:DD:EE:FF connected.
"""

#mac_pattern = r"(?:[0-9a-fA-F]{2}[:-]){5}[0-9a-fA-F]{2}"
m = re.findall(r'(?:[0-9a-fA-F]{2}[:.-]){5}[0-9a-fA-F]{2}', log)
print(m)