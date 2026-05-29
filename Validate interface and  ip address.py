string ='''Windows IP Configuration

Ethernet adapter Ethernet:
 
   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
 
Wireless LAN adapter Local Area Connection* 1:
 
   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
 
Wireless LAN adapter Local Area Connection* 2:
 
   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
 
Wireless LAN adapter Wi-Fi:
 
   Connection-specific DNS Suffix  . :
   IPv6 Address. . . . . . . . . . . : 2406:7500:63:43e4:xg5c:ca17:5f3b:9e1d
   Temporary IPv6 Address. . . . . . : 2406:7800:63:43e4:fx9f:6ba2:5c42:2c5c
   Link-local IPv6 Address . . . . . : fe80::100a:710:ex64:d89d%18
   IPv4 Address. . . . . . . . . . . : 192.168.0.3
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : fx80::3e78:95ff:fece:e7aa%18
                                       192.168.0.1
 
Ethernet adapter Bluetooth Network Connection:
 
   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :'''
import re
  #user_input_interface = input("enter the interface name by user")
  #user_input_ip_address = input("enter the ip add of interface by user")
ip_pattern =r'(\w+\s+\w+)[. :]+((?:\d{1,3}\.){3}\d{1,3})'
interface_output = re.findall(ip_pattern, string)
 #interface_ip_address_output = re.findall(ip_pattern, string)
print(interface_output)

 
 
 