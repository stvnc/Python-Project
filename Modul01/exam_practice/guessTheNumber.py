import random

generatedRandomNumber = random.randint(0,20)
status = False
count = 0

while status == False and count < 5:
    print(f'Chances left: {5-count}')
    userInput = int(input('Guess the number: '))
    if userInput > generatedRandomNumber:
        print("Too High")
    elif userInput < generatedRandomNumber:
        print("Too Low")
    else:
        print("You're Correct!")
        status = True
    count += 1