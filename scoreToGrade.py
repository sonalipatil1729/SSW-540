print("**Know your grade**")
try:
  score = float(input("Please enter your Quiz Score: "))
  if(score>=93 and score<100):
   print("Your grade is A")
  elif (score>=90 and score<93):
   print("Your grade is A-")
  elif(score>=87 and score<90):
   print("Your grade is B+")
  elif(score>=83 and score<87):
   print("Your grade is B")
  elif(score>=80 and score<83):
   print("Your grade is B-")
  elif(score>= 70 and score<80):
   print("Your grade is C")
  elif(score>=100 or score<0):
   print("Please enter valid score(0-100)")
  else:
   print("Your grade is F")
except Exception as e:
   print("Wrong input. Please enter correct score")
