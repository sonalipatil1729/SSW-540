import os
import time
import sys
import re
print "*****Program to demonstrate the use of Regular Expression*****"
fileName = raw_input("Enter the file name: ")
revisionList = list()
count = 0
average = 0.0
try:
 fHandle = open(fileName,'r')
except IOError:
 print "Error: can\'t find file or read data"
 sys.exit()
if os.stat(fileName).st_size != 0: #to chekc if file is not empty
 for line in fHandle:
  revision = re.findall('^New Revision: ([0-9]+)',line)
  if len(revision) != 1: #if no match found continue to next iteration
  	continue
  count += 1
  number = int(revision[0])
  revisionList.append(number)
 try:
  average = round(sum(revisionList,0.0)/float(len(revisionList)),1)
 except:
  print "File does not have any line with New Revision."
  sys.exit()
 print "Average = ", average
 print "Number of lines = ", count
else:
 print"This file is empty"