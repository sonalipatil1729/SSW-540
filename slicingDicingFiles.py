# Python program for file handling

import os
import time
import sys

print "*****Program to find the Average Spam Confidence Value*****"
fileName = raw_input("Enter the file name: ")
try:
    fHandle = open(fileName, 'r')
except IOError:
    print "Error: can\'t find file or read data"
    sys.exit()
if os.stat(fileName).st_size != 0:  # to chekc if file is not empty
    countOfLines = 0.0
    sumOfConfidence = 0.0
    for line in fHandle:
        if line.startswith("X-DSPAM-Confidence:"):
            str = line[line.find(":") + 1:].lstrip()
            confidenceValue = str[:str.find(' ')].strip()
            # confidence value cou;ld contain corrupted value
            try:
                confidenceValue = float(confidenceValue)
                countOfLines += 1
                sumOfConfidence += confidenceValue
            except ValueError:
                print "Not a valid value:", confidenceValue
    # calculating the average of confidence
    try:
        average = sumOfConfidence / countOfLines
    except ZeroDivisionError:
        print"No rows found with X-DSPAM-Confidence"
        sys.exit()
    print("Average spam confidence: %.4f " % average)
    fHandle.close()
else:
    print"This file is empty"

