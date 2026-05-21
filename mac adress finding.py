import re

# Sample text containing three device MAC addresses
network_log = """
Device 1 (Router): 00:1A:2B:3C:4D:5E connected 
Device 2 (Switch): 1A-2B-3C-4D-5E-6F connected 
Device 3 (Laptop): AA:BB:CC:DD:EE:FF connected
"""
#mac_pattern = r"(?:[0-9a-fA-F]{2}[:-]){5}[0-9a-fA-F]{2}"
mac_pattern = r"([0-9a-fA-F]{2}[:-]){5}[0-9a-fA-F]{2}"
split_log = network_log.strip().splitlines()
print(split_log)
# Loop until no more matches are found or we reach our target count
for line in split_log:
    # Use re.search() on a sliced version of the text to advance the window
    match = re.search(mac_pattern, line)
    if not match:
        break  # Stop if no more MAC addresses are found   
    print(f"Device Found: {match.group()}")
    # Update the position pointer to look past the current match

log = """
Device 1 (Router): 00.1A.2B.3C.4D.5E connected.
Device 2 (Switch): 1A-2B-3C-4D-5E-6F connected.
Device 3 (Laptop): AA:BB:CC:DD:EE:FF connected.
"""
import re
pattern = r'(?:[0-9a-fA-F]{2}[.:-]){5}[0-9a-fA-F]{2}'
#pattern = r'(?:[0-9a-fA-F]{2}[.:-])+[0-9a-fA-F]+'
match = re.findall(pattern,log)
print(match)

log1 = '''FastEthernet0/0 is administratively down, line protocol is down Hardware is DEC21140, address is ca01.3cd1.0000 (bia ca01.3cd1.0000)'''

#pattern = r'(?:[0-9a-fA-F]{4}[.]){2}[0-9a-fA-F]{4}'
pattern = r'(?:[0-9a-fA-F]{4}[.]){2}[0-9a-fA-F]+'
match = re.findall(pattern,log1)
print(match)
