import netifaces
import re
import os
import sys

def find():
   no = []
   os.system("clear")
   interface = netifaces.interfaces()
   for iface in interface:
      yes = re.findall("wlan[0-9]", iface)
      if yes:
         no.append(yes)
      else:
         pass
   if len(no) == 0:
      print("Please bring another up interface and try again")
   else:
      print(no)

find()
