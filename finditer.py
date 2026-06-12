import re

log = "IP is 10.168.1.15"

ip_pat = r'\b((25[0-5]|2[0-4]\d|1?\d{1,2})\.){3}(25[0-5]|2[0-4]\d|1?\d{1,2})\b'
matches = [m.group(0) for m in re.finditer(ip_pat, log)]
print(matches)
ip_pat = r'\b(?:(?:25[0-5]|2[0-4]\d|1?\d{1,2})\.){3}(?:25[0-5]|2[0-4]\d|1?\d{1,2})\b'
matches = [m for m in re.findall(ip_pat, log)]
print(matches)

# re.findall(), which loads all matched text strings into memory at once as a list, 
# re.finditer() processes matches lazily (one by one).
ip_pat = r'\b(?:(?:25[0-5]|2[0-4]\d|1?\d{1,2})\.){3}(?:25[0-5]|2[0-4]\d|1?\d{1,2})\b'
matches =  re.findall(ip_pat, log)
print(matches)