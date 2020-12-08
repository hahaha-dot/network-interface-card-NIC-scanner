import netifaces
import re
import os
import sys

if os.getuid() == 0:   #To check whether the user run as root
   pass
else:
   sys.exit("please run as root")     #Exit the program and print the message

def find():
   no = []     #create a empty list
   os.system("clear")
   interface = netifaces.interfaces()    #get the available interface
   for iface in interface:
      yes = re.findall("wlan[0-9]", iface)
      if yes:
         no.append(yes)      #append the yes to the empty list
      else:
         pass
   if len(no) == 0:       #to check whether the empty list is empty or not, if empty leave, to determine is there any interface in the no list, if empty leave
      sys.exit("Please bring another up interface and try again")
   else:
      print(no)

find()
