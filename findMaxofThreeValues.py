"""Name: Sonali Patil
This program will generate a random number and will ask user to guess the number in 6 guesses.
The program is coded to handle all the below use cases:
- if user provides incorrect input(alphabet): program will give message to user that input is not correct and will ask again to input correct value
- if user provides incorrect input(number beyond the specified range): program will give message to user that input is not correct and will ask again to input correct value in valid range
- if user guesses the number in <6 chances, program will ask user if he wants to continue playing or exit
- if user does not guess the number in 6 gueasses, program will tell the user which was the generated number and will ask for choices to continue  or to exit. 
Note: User will have 6 chances to guess the number excluding the attempts where he has put incorrect value i.e. number out of range, and non digit number.
"""
import random


def init():
    startThegame()
    nextActivity()


def nextActivity():
    activity = raw_input("\nDo you want to start over(Y/N)?")
    if activity == 'Y' or activity == 'y':
        init()
    elif activity == 'N' or activity == 'n':
        exit()
    else:
        print "Please enter correct choice"
        nextActivity()


def startThegame():
    print("Well," + name + ", I am thinking of a number between 1 and 20.\n")
    randomNumber = random.randint(1, 20)
    i = 1
    while (i <= 6):
        try:
            guessedNumber = int(raw_input("Take a guess: "))
        except Exception as e:
            print("Please enter the correct number \n")
            continue  # so that user will have exact 6 chances to input correct value
        if isInRange(guessedNumber) == 1:
            print "Please Enter the number which is 20< or >1\n"
            continue  # so that user will have exact 6 chances to input correct value
        result = isTheGuessCorrect(guessedNumber, randomNumber)
        if result == 0:
            print("Good job," + name + "! You guessed my number in " + str(i) + " guesses!")
            break
        elif result == -1:
            print("Your guess is too low.\n")
        elif result == 1:
            print("Your guess is too high.\n")
        i = i + 1  # to iterate the loop
    if i > 6:
        print("You have not guessed the number correctly!!!The number I was thinking of was " + str(randomNumber))


def isTheGuessCorrect(guessedNumber, randomNumber):
    if guessedNumber == randomNumber:
        return 0
    elif guessedNumber < randomNumber:
        return -1
    elif guessedNumber > randomNumber:
        return 1


def isInRange(guessedNumber):
    if guessedNumber < 1 or guessedNumber > 20:
        return 1
    else:
        return 0


# Program will start from here
print("*****Guess the Number Game*****\n")
name = raw_input("Hello! What is your name? ")
init()
