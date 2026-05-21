log = '''System log found on 12/05/2026. The workstation XTZ-9812 has a 
MAC address of 00-1A-2B-3C-4D-5E. The IPv4 address is 192.168.1.15 
and the IPv6 address is 2001:0db8:85a3:0000:0000:8a2e:0370:7334. 
The device serial is SN998877A. The registered employee is John Doe (ID: EMP-0452).
Please reach out via john.doe@company.com or +91-9876543210. 
Verify tax documents at 560001 with PAN ABCDE1234F.'''
import re
ipv4_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
match = re.findall(ipv4_pattern, log)
print(match)
valid_ipv4_pattern = r'\b(?:(?:25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.){3}(?:25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\b'
match = re.findall(valid_ipv4_pattern, log)
print(match)
valid_ipv4_pattern1 = r'((25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})'
rusult = re.search(valid_ipv4_pattern1, log)
print(rusult.group())
valid_ipv4_pattern2 = r'((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})'
match = re.search(valid_ipv4_pattern2, log)
print(match.group())
ipv6_pattern = r'\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b'
match = re.findall(ipv6_pattern, log)
print(match)
mac_address_pattern = r'\b(?:[0-9a-fA-F]{2}[:-]){5}[0-9a-fA-F]{2}\b'
match = re.findall(mac_address_pattern, log)
print(match)
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
match = re.findall(email_pattern, log)
print(match)
phone_no_pattern = r'\+\d{1,3}-\d{10}'
match = re.findall(phone_no_pattern, log)
print(match)
pan_pattern = r'\b[A-Z]{5}\d{4}[A-Z]\b'
match = re.findall(pan_pattern, log)
print(match)
pin_code_pattern = r'\b\d{6}\b'
match = re.findall(pin_code_pattern, log)
print(match)
date_pattern = r'\b\d{2}\/\d{2}\/\d{4}\b'
match = re.findall(date_pattern, log)
print(match)
serial_no_pattern = r'\bSN\d{6}[A-Z]\b'
match = re.findall(serial_no_pattern, log)
print(match)
employee_id_pattern = r'\bEMP-\d{4}\b'
match = re.findall(employee_id_pattern, log)
print(match)