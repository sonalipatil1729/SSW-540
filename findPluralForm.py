# The program asks user for the words for which he/she wants to see the plural form of those words.
# The script will print the string with plural forms only for correct words.
import string
def init():
 input = raw_input("Please enter the string(s): ")
 if len(input)<=1:
  print("\nOOps!!!Please enter correct string which contains atleast one word only\n")
  init()
 words = input.split()                                # split will devide the line into words seperated by space
 result = ''
 invalid =''
 pluralWord = ''
 for word in words:
  pluralWord = plural(word)
  if word == pluralWord:
   invalid = (" ".join([invalid,pluralWord]))
  else:
   result = (" ".join([result,pluralWord]))

 print "\nPlural form for valid Strings: "+result
 print "List of invalid strings: "+invalid
 nextActivity()

def nextActivity():
 activity =raw_input("\nDo you want to start over(Y/N)?")
 if activity=='Y'or activity=='y':
  init()
 elif activity=='N' or activity =='n':
  exit()
 else:
  print "Please enter correct choice"
  nextActivity()

def plural(word):
 if hasDigitInString(word) or hasSpecialCharInString(word):
  return word
 if word.endswith(('ay','ey','iy','oy','uy')):
  word = word+'s'
 elif word.endswith('y'):
  word = word[:-1]
  word = word+'ies'
 elif word.endswith(('o','ch','s','sh','x','z')):
  word = word+'es'
 else:
  word = word+'s'
 return word

def hasDigitInString(inputString):
 return any(char.isdigit() for char in inputString)

def hasSpecialCharInString(inputString):
 return any(char in string.punctuation for char in inputString)


print("*****String Manipulations*****")
init()



