# Python program for finding Unique values in a file
# Using set to store the unique values

import os
import time
import sys

print "*****Program to find the unique email addresses*****"
fileName = raw_input("Enter the file name: ")
try:
    fHandle = open(fileName, 'r')
except IOError:
    print "Error: can\'t find file or read data"
    sys.exit()
if os.stat(fileName).st_size != 0:  # to chekc if file is not empty
    countOfUnique = 0
    items = set()
    for line in fHandle:
        if line.startswith("From:"):
            email = line.split(":")[1].split()
            # email = str[1]
            # email = email.split()
            if email[0].find("@"):
                items.add(email[0])
    countOfUnique = len(items)
    if countOfUnique > 0:
        print "Number of unique addresses in " + fileName + " is ", countOfUnique
    else:
        print "File does not contain any sender's email address."
else:
    print"Oops!!!This file is empty"

