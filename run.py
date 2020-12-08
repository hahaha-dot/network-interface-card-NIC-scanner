import netifaces
import re
import os
import sys

def find():
   os.system("clear")
   interface = netifaces.interfaces()
   print(interface)
   for iface in interface:
      yes = re.findall("wlan[0-9]", iface)
      if yes:
         print(yes)
      else:
         print("please try again")

find()
