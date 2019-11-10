import random

generatedRandomNumber = random.randint(0,20)
status = False

while status == False:
    userInput = int(input('Guess the number: '))
    if userInput > generatedRandomNumber:
        print("Too High")
    elif userInput < generatedRandomNumber:
        print("Too Low")
    else:
        print("You're Correct!")
        status = True
