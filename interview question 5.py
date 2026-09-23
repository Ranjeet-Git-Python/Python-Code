import re
output = '''Auto-upgrade:Enabled,PM excluded
Attribute codes: B golden, P protect, S secure, A Anti Theft aware
                                                                         FPD Versions
                                                                        ==============
Location   Card type             HWver FPD device       ATR Status    Running  Programd   Reload Loc
-------------------------------------------------------------------------------------------------
0/RP0/CPU0 8011-16G8X-A          0.1   BckUp-BootLoader BS  CURRENT               1.05          0/RP0
0/RP0/CPU0 8011-16G8X-A          0.1   IoFpga               CURRENT      1.08     1.08          0/RP0
0/RP0/CPU0 8011-16G8X-A          0.1   IoFpgaGolden     B   NEED UPGD             1.03          0/RP0
0/RP0/CPU0 8011-16G8X-A          0.1   Prim-BootLoader  S   CURRENT      1.05     1.05          0/RP0
0/RP0/CPU0 8011-16G8X-A          0.1   StdbyFpga        S   CURRENT      0.28     0.28          0/RP0
0/RP0/CPU0 8011-16G8X-A          0.1   StdbyFpgaGolden  BS  NEED UPGD             0.20          0/RP0
RP/0/RP0/CPU0:sabot_p'''
# output1 = output.splitlines()
# #print(output1)
# for i in output1:
#   pattern  = r'\s+(\S+)\s+\S+\s+(\S+)\s+'
#   #match = re.search(pattern,i)
#   #print(match.group(0))
#   match = re.findall(pattern,i)
#   #print(match.group(0))
#   print(match)
import re
# pattern = r"^\s*\S+\s+\S+\s+\S+\s+(\S+)\s+(?:\S+\s+)?(CURRENT|NEED\s+UPGD)"
# for line in output.splitlines():
#     match = re.search(pattern, line)
#     if match:
#         fpd_device, status = match.groups()
#         print(f"FPD device: {fpd_device}, Status: {status}")

result = []
for line in output.splitlines():
  m = re.search(r'(\S+)\s+(?:\S+\s+)?(CURRENT|NEED UPGD)', line)
  if m:
    result.append({
      "fpd_device": m.group(1),
      "status": m.group(2)
      })
print(result)