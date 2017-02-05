#Python program for finding the sender with highest number of sent mails
#Using Dictionary to store the sender and count values
import os
import time
import sys
print "*****Program to find the unique email addresses*****"
fileName = raw_input("Enter the file name: ")
try:
 fHandle = open(fileName,'r')
except IOError:
 print "Error: can\'t find file or read data"
 sys.exit()
if os.stat(fileName).st_size != 0: #to chekc if file is not empty
 senders = dict()
 for line in fHandle:
  if line.startswith("From:"):
   email = line.split(":")[1].split()
   if email[0].find("@"):
    senders[email[0]] = senders.get(email[0],0)+1
 highestCount = 0
 moreEmailSender = 0
 for email,count in senders.items():
  if highestCount is 0 or highestCount < count:
   moreEmailSender = email
   highestCount = count
 if moreEmailSender is not 0 and highestCount > 0:
  print "Most mails are sent by",moreEmailSender
  print "Number of mails sent is",highestCount
 else:
  print "File does not contain any sender's email address."
else:
 print"Oops!!!This file is empty"