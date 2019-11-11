import random

status = False

matchRound = int(input('How many round do you desire?: '))
count = 1

while count <= matchRound:
    computerMove = random.randint(1,3)
    print(f'Round {count}')
    userMove = int(input('Choose 1 for Rock, 2 for Paper, and 3 for Scissor: '))
    print(f'Computer: {computerMove}, You: {userMove}')
    if (userMove == 1 and computerMove == 2) or (userMove == 2 and computerMove == 3) or (userMove == 3 and computerMove == 1):
        print("You Lose!")
    elif userMove == computerMove:
        print("Draw!")
    else:
        print("You Win!")
    count += 1
